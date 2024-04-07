import pygame
import random
from pygame import Vector2, Rect

class Enemy:
    def __init__(self, pos: Vector2, speed):
        self.pos = pos.copy()
        self.speed = speed
        self.extents = Rect(-10, -10, 20, 20)
        self.rect = self.extents.move(self.pos.x, self.pos.y)
        self.destroyed = False
        
        # List of possible sprite paths
        sprite_options = ["assets\PNG\Enemies\enemyGreen1.png",
                          "assets\PNG\Enemies\enemyGreen2.png",
                          "assets\PNG\Enemies\enemyGreen3.png",
                          "assets\PNG\Enemies\enemyGreen4.png",
                          "assets\PNG\Enemies\enemyGreen5.png",
                          ]
        # Randomly select on of the sprites
        random_sprite = random.choice(sprite_options)
        
        # Load and scale the sprites
        sprite = pygame.image.load(random_sprite).convert_alpha()
        self.sprite = pygame.transform.scale(sprite, (30,30))
        
        # Adjust the rectangle to match the sprite size
        self.rect = self.sprite.get_rect(topleft=self.pos)
        
    
    def update(self, dt):
        self.pos += Vector2(0, self.speed) * dt
        self.rect = self.extents.move(self.pos)

    def draw(self, surface):
        #pygame.draw.rect(surface, "#DC143C", self.rect)  # Crimson color
        surface.blit(self.sprite, self.rect.topleft)