import pygame
from constants import *
import random

from circleshape import CircleShape

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, self.radius)
            a2 = Asteroid(self.position.x, self.position.y, self.radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2