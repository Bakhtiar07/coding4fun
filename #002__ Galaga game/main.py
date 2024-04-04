import pygame
from pygame import Vector2, Rect
import numpy as np

class Ship:
    def __init__(self, pos: Vector2):
        self.original_pos = pos.copy()
        self.pos = pos
        self.extents = Rect(-10, -10, 20, 20)
        self.rect = self.extents.move(self.pos.x, self.pos.y)
    
    def reset(self):
        self.pos = self.original_pos.copy()
        self.update_rect()

    def update(self, dt, left: float, right: float, window_width):
        self.pos += (right - left) * Vector2(300, 0) * dt
        self.pos.x = pygame.math.clamp(self.pos.x, 0, window_width - self.extents.width)
        self.update_rect()
        
    def update_rect(self):
        self.rect = self.extents.move(self.pos.x, self.pos.y)

    def draw(self, surface):
        pygame.draw.rect(surface, "#FFD700", self.rect)  # Gold color for the ship

class Enemy:
    def __init__(self, pos: Vector2, speed):
        self.pos = pos
        self.speed = speed
        self.extents = Rect(-10, -10, 20, 20)
        self.rect = self.extents.move(self.pos.x, self.pos.y)
    
    def update(self, dt, window_height):
        self.pos += Vector2(0, self.speed) * dt
        self.update_rect()
        
    def update_rect(self):
        self.rect = self.extents.move(self.pos.x, self.pos.y)

    def draw(self, surface):
        pygame.draw.rect(surface, "#DC143C", self.rect)  # Crimson color for obstacles

class Projectile:
    def __init__(self, pos: Vector2, speed: float):
        self.pos = pos.copy()
        self.speed = speed
        self.direction = Vector2(0, -3)
        self.rect = Rect(self.pos.x - 2, self.pos.y - 5, 4, 10)

    def update(self, dt):
        self.pos += self.speed * self.direction * dt
        self.update_rect()
        
    def update_rect(self):
        self.rect = Rect(self.pos.x - 2, self.pos.y - 5, 4, 10)

    def draw(self, surface):
        pygame.draw.rect(surface, "#FFFFFF", self.rect)  # White for projectiles

def reset_game():
    global enemies, projectiles, ship, score
    enemies = []
    projectiles = []
    ship.reset()
    score = 0

pygame.init()

window_size = (640, 480)
main_surface = pygame.display.set_mode(window_size, pygame.SCALED | pygame.RESIZABLE, vsync=1)
font = pygame.font.Font(None, 36)

running = True
enemies = []
projectiles = []
ship = Ship(Vector2(320, 440))
score = 0
clock = pygame.time.Clock()

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                projectiles.append(Projectile(Vector2(ship.pos.x, ship.pos.y - 10), 300))
            if evt.key == pygame.K_r:
                reset_game()

    dt = clock.tick(60) / 1000

    if np.random.rand() < 0.02:  # Adjust frequency of obstacles
        enemies.append(Enemy(Vector2(np.random.rand() * 640, -20), 100))

    keys = pygame.key.get_pressed()
    ship.update(dt, 1 if keys[pygame.K_a] else 0, 1 if keys[pygame.K_d] else 0, window_size[0])
    
    for p in projectiles:
        p.update(dt)
    for e in enemies:
        e.update(dt, window_size[1])

    # Check for projectile-obstacle collisions
    for projectile in projectiles[:]:
        for enemy in enemies[:]:
            if projectile.rect.colliderect(enemy.rect):
                projectiles.remove(projectile)
                enemies.remove(enemy)
                score += 10
                break

    # Check for ship-obstacle collisions
    for enemy in enemies[:]:
        if ship.rect.colliderect(enemy.rect):
            reset_game()  # Reset the game if the ship collides with an obstacle

    # Remove off-screen projectiles
    projectiles = [p for p in projectiles if p.pos.y > 0]

    main_surface.fill("#000000")
    ship.draw(main_surface)
    for p in projectiles:
        p.draw(main_surface)
    for e in enemies:
        e.draw(main_surface)
    
    # Draw score
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    main_surface.blit(score_surface, (10, 10))

    pygame.display.flip()
