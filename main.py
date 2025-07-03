# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from astroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable , drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    astroidfield = AsteroidField()


    while True:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        dt = clock.tick() / 1000
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        clock.tick(60)

        for obj in asteroids:
            if obj.collision(player):
                sys.exit("Game Over!")
            for bullet in shots:
                if obj.collision(bullet):
                    bullet.kill()
                    obj.split()
        
        screen.fill("black")


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
