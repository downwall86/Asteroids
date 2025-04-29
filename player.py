import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-0.05)
            # ?
        if keys[pygame.K_d]:
            self.rotate(0.05)
            # ?

        if keys[pygame.K_w]:
            self.move(0.05)

        if keys[pygame.K_s]:
            self.move(-0.05)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Create a new shot at the player's position
        new_shot = Shot(self.position.x, self.position.y)
    
        # Set the shot's velocity based on player direction
        # Start with (0, 1) vector
        # Rotate it to match player's angle
        # Scale it by PLAYER_SHOOT_SPEED
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)  # Negative because pygame rotations are clockwise
        new_shot.velocity = direction * PLAYER_SHOOT_SPEED
    
        # Add to shots group
        # shots.add(new_shot)  # You'll need to access your shots group