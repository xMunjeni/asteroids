import pygame, random
from logger import log_state, log_event
from circleshape import CircleShape
from constants import *

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
            random_offset = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity_1 = pygame.math.Vector2.rotate(self.velocity, random_offset)*1.2
            new_velocity_2 = pygame.math.Vector2.rotate(self.velocity, -random_offset)*1.2
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_velocity_1
            new_asteroid_2.velocity = new_velocity_2