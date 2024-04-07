import pygame
import random
from pygame import Vector2, Rect

class Asteroid:
    def __init__(self, pos: Vector2, speed):
        self.pos = pos.copy()
        self.speed = speed
        self.health = 100
        self.destroyed = False
        
        # Load and scale the sprites
        intial_sprite = pygame.image.load("assets\PNG\Meteors\meteorBrown_med1.png").convert_alpha()
        damaged_sprite = pygame.image.load("assets\PNG\Meteors\meteorBrown_small1.png").convert_alpha()
        self.initial_sprite = pygame.transform.scale(intial_sprite, (35,35)) # Scale the image.
        self.damaged_sprite = pygame.transform.scale(damaged_sprite, (25,25))
        
        # Adjust the rectangle to match the sprite size
        self.sprite = self.initial_sprite
        self.rect = self.sprite.get_rect(center=self.pos)
        
    def update(self, dt):
        self.pos += Vector2(0,self.speed)*dt
        
        # Update sprite based on health
        if self.health < 100:
            self.sprite = self.damaged_sprite
        else:
            self.sprite = self.initial_sprite
            
        #self.extents = Rect(-10,-10, self.health/4, self.health/4)
        #self.rect = self.extents.move(self.pos)
        self.rect = self.sprite.get_rect(center=self.pos)
        
        # Check if the asteroid is destroyed based on health
        if self.health <= 0:
            self.destroyed = True

    def draw(self, surface):
        if not self.destroyed:
            #pygame.draw.rect(surface,"#A9A9A9",self.rect)
            surface.blit(self.sprite, self.rect.center)
        