import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            asteroid1_angle = self.velocity.rotate(random_angle)
            asteroid2_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid_1.velocity = asteroid1_angle * 1.2
            Asteroid_2.velocity = asteroid2_angle * 1.2
