import pygame
import constants
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, radius=self.radius, width=2 )
        pass
    
    def update(self, dt):
        self.position += (self.velocity * dt)