import pygame
import numpy as np
import time
from pygame import Vector2, Rect
from Player import Player 
from Enemy import Enemy
from Asteroid import Asteroid
from Missile import Missile


class Game:
    def __init__(self):
        self.missiles:list[Missile] = []
        self.player = Player(Vector2(screen_width/2, screen_height - 20))
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

pygame.quit()
