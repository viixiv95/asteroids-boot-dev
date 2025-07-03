from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-1*random_angle)
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astroid = Asteroid(self.position.x, self.position.y, new_radius)
        astroid.velocity = new_velocity1 * 1.2
        astroid = Asteroid(self.position.x, self.position.y, new_radius)
        astroid.velocity = new_velocity2 * 1.2
 
        
        
