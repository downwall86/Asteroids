import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, radius=self.radius, width=2 )
        pass
    
    def update(self, dt):
        self.position += (self.velocity * dt)
'''
    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_asteroid = Asteroid(self.x, self.y, old_radius - ASTEROID_MIN_RADIUS)
            new_asteroid.velocity = pygame.Vector2.rotate(self.velocity, random_angle) * 1.2
            new_asteroidtwo = Asteroid(self.x, self.y, old_radius - ASTEROID_MIN_RADIUS)
            new_asteroidtwo.velocity = pygame.Vector2.rotate(self.velocity, -random_angle) * 1.2
'''
