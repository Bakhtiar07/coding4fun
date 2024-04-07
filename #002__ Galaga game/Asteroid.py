import pygame
from pygame import Vector2, Rect

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