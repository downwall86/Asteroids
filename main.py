import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    playerone = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    stillrunning = 1
    clock = pygame.time.Clock()
    dt = 0
    while stillrunning == 1:
        screen.fill((0, 0, 0))
        playerone.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        dt = (clock.tick(60)) / 1000
      



if __name__ == "__main__":
    main()