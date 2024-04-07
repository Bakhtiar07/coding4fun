import pygame
from pygame import Vector2, Rect

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
