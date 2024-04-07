import pygame
from pygame import Vector2, Rect

class Player:
    def __init__(self, pos: Vector2):
        self.original_pos = pos.copy()
        self.pos = pos
        self.extents = Rect(-10, -10, 40, 25)
        self.destroyed = False
        
        # Load and scale the sprite        
        sprite = pygame.image.load('assets/PNG/playerShip1_orange.png').convert_alpha()
        self.sprite = pygame.transform.scale(sprite, (45,30))
        
        # Adjust the rectangle to match the sprite size
        self.rect = self.sprite.get_rect(topleft=self.pos)
        
    def update(self, dt, left: float, right: float, window_width):
        self.pos += (right - left) * Vector2(300, 0) * dt
        self.pos.x = pygame.math.clamp(self.pos.x, 0, window_width - self.extents.width)
        self.update_rect()
        
    def update_rect(self):
        #self.rect = self.extents.move(self.pos.x, self.pos.y)
        self.rect.topleft = self.pos

    def draw(self, surface):
        #pygame.draw.rect(surface, "#FFD700", self.rect)  # Gold color 
        surface.blit(self.sprite, self.rect.topleft)
