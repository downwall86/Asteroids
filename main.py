import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the two required groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set these groups as containers for the Player class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    

    playerone = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    AstField = AsteroidField()
    
    stillrunning = 1
    clock = pygame.time.Clock()
    dt = 0
    while stillrunning == 1:
        #print(f"dt: {dt}, movement: {PLAYER_SPEED * dt}")
        screen.fill((0, 0, 0))
        
        # old# playerone.update(dt)
        # old# playerone.draw(screen)

         # Update all objects in the updatable group
        updatable.update(dt)

        for asteroid in asteroids:  # This creates a variable called 'asteroid' for each item in 'asteroids'
    # Check player collision
            if playerone.collisionCheck(asteroid) == True:
                print("Game Over!")
                pygame.quit()
                sys.exit()
    
    # For each asteroid, check collision with each bullet
            for bullet in shots:
                if bullet.collisionCheck(asteroid) == True:
                    print("hit")
                    bullet.kill()
                    AstField.split_asteroid(asteroid)
            
        
        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)


        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        dt = (clock.tick(60)) / 1000
        dt = min(dt, 0.033)
      



if __name__ == "__main__":
    main()