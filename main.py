import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ragdoll settings
class Ragdoll:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.points = []
        self.create_ragdoll()

    def create_ragdoll(self):
        for _ in range(5):
            point = (self.x + random.randint(-10, 10), self.y + random.randint(-10, 10))
            self.points.append(point)

    def draw(self, screen):
        for point in self.points:
            pygame.draw.circle(screen, BLACK, point, self.radius)

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ragdoll Physics Game')
    clock = pygame.time.Clock()
    ragdoll = Ragdoll(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        ragdoll.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()