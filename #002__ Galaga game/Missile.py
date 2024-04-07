import pygame
from pygame import Vector2, Rect

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
