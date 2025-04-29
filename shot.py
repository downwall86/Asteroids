import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
        containers = None  # This will be set later

        def __init__(self, x, y):
            super().__init__(x, y, SHOT_RADIUS)
            self.velocity = pygame.Vector2(0, 0)  # Initialize velocity, will be set by player

            # Add self to all containers
            if Shot.containers:
                for container in Shot.containers:
                    container.add(self)



        def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, radius=self.radius, width=2 )
        
    
        def update(self, dt):
            self.position += (self.velocity * dt)