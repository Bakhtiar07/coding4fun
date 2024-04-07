import pygame
from pygame import Vector2, Rect
import numpy as np
import time

class Player:
    def __init__(self, pos: Vector2):
        self.original_pos = pos.copy()
        self.pos = pos
        self.extents = Rect(-10, -10, 20, 20)
        self.destroyed = False
        self.rect = self.extents.move(self.pos.x, self.pos.y)

    def update(self, dt, left: float, right: float, window_width):
        self.pos += (right - left) * Vector2(300, 0) * dt
        self.pos.x = pygame.math.clamp(self.pos.x, 0, window_width - self.extents.width)
        self.update_rect()
        
    def update_rect(self):
        self.rect = self.extents.move(self.pos.x, self.pos.y)

    def draw(self, surface):
        pygame.draw.rect(surface, "#FFD700", self.rect)  # Gold color 

class Enemy:
    def __init__(self, pos: Vector2, speed):
        self.pos = pos
        self.speed = speed
        self.extents = Rect(-10, -10, 20, 20)
        self.rect = self.extents.move(self.pos.x, self.pos.y)
        self.destroyed = False
    
    def update(self, dt):
        self.pos += Vector2(0, self.speed) * dt
        self.rect = self.extents.move(self.pos)

    def draw(self, surface):
        pygame.draw.rect(surface, "#DC143C", self.rect)  # Crimson color

class Asteroid:
    def __init__(self, pos: Vector2, speed):
        self.pos = pos
        self.speed = speed
        self.health = 100
        self.destroyed = False
        
    def update(self, dt):
        self.pos += Vector2(0,self.speed)*dt
        self.extents = Rect(-10,-10, self.health/5, self.health/5)  
        self.rect = self.extents.move(self.pos)

    def draw(self, surface):
        pygame.draw.rect(surface,"#00FFFF",self.rect)

class Missile:
    def __init__(self, pos: Vector2, speed: float):
        self.pos = pos.copy()
        self.speed = speed
        self.direction = Vector2(0, -2)
        self.extents = Rect(-1,1,2,4)
        self.destroyed = False

    def update(self, dt):
        self.pos += self.speed * self.direction * dt
        self.rect = self.extents.move(self.pos)
        
    def draw(self, surface):
        pygame.draw.rect(surface, "#FFFFFF", self.rect, width=1)  # White color

class Game:
    def __init__(self):
        self.missiles:list[Missile] = []
        self.player = Player(Vector2(screen_width/2, screen_height-50))
        self.score = 0
        self.enemies:list[Enemy] = []
        self.asteroids:list[Asteroid] = []
        self.state = "PLAYING"
        self.reset_time = 3
        self.end_time = 0

pygame.init()

running = True
screen_width, screen_height = 640, 480
main_surface = pygame.display.set_mode((screen_width,screen_height), pygame.SCALED | pygame.RESIZABLE, vsync=1)
font = pygame.font.Font(pygame.font.get_default_font(), 36) # initialize a system font
clock = pygame.time.Clock()
G = Game()

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_p:
                if G.state == "PLAYING":
                    G.state = "PAUSED"
                elif G.state == "PAUSED":
                    G.state = "PLAYING"
            if evt.key  == pygame.K_SPACE and G.state == "PLAYING":
                G.missiles.append(Missile(Vector2(G.player.pos.x, G.player.pos.y - 10),300))                

    # Calculate delta time
    dt = clock.tick(60) / 1000 # advance the tick
    
    keys = pygame.key.get_pressed()
    G.player.update(dt, 1 if keys[pygame.K_a] else 0, 1 if keys[pygame.K_d] else 0, screen_width)

    if G.state == "PLAYING":
        # spawn enemies and asteroids randomly
        if np.random.rand() < .01:
            G.enemies.append(Enemy(Vector2(np.random.rand()*700+50,20),50))
        if np.random.rand() < .05:
            G.asteroids.append(Asteroid(Vector2(np.random.rand()*700+50,20),50))

        for m in G.missiles:
            m.update(dt)
        for e in G.enemies:
            e.update(dt)
        for a in G.asteroids:
            a.update(dt)

        # detect collisions and handle effects
        # do any of the missiles hit any of the enemies?
        for m in G.missiles:
            if m.pos.y < 0:
                m.destroyed = True
            for e in G.enemies:
                if m.rect.colliderect(e.rect):
                    m.destroyed = True
                    e.destroyed = True
                    G.score += 1
            for a in G.asteroids:
                if m.rect.colliderect(a.rect):
                    m.destroyed = True
                    a.health -= 50 # reduce the health

        # do any of the asteroids or enemies hit the player
        for a in G.asteroids:
            if a.rect.colliderect(G.player.rect):
                G.player.destroyed = True
        for e in G.enemies:
            if e.rect.colliderect(G.player.rect):
                G.player.destroyed = True
                
        # remove any missiles or enemies that have been destroyed
        G.missiles = list(filter(lambda x: x.destroyed == False, G.missiles))
        G.enemies = list(filter(lambda x: x.destroyed == False, G.enemies))
        G.asteroids = list(filter(lambda x: x.health > 0, G.asteroids))
        if G.player.destroyed:
            G.end_time = time.time()
            G.state = "GAME OVER"
            
        # draw everything
        main_surface.fill("#000000")
        G.player.draw(main_surface)
        for m in G.missiles:
            m.draw(main_surface)
        for e in G.enemies:
            e.draw(main_surface)
        for a in G.asteroids:
            a.draw(main_surface)
    
        # Draw score
        score_surface = font.render(f"Score: {G.score}", True, "#FFFFFF")
        main_surface.blit(score_surface, (5, 5))
        
    elif G.state == "GAME OVER":

        if time.time() - G.end_time > G.reset_time:
            G = Game() # easy way to reset!

        t = font.render(f"Game Over!", True, "#FFFFFF")
        x,y = t.get_rect().center
        main_surface.blit(t,(screen_width/2-x, screen_height/2-y))
    
    elif G.state == "PAUSED":
        pass # just do nothing!

    pygame.display.flip()
