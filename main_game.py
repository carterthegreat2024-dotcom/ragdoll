import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.velocity = 0
        self.health = 100
        self.is_ragdoll = False

    def update(self):
        if not self.is_ragdoll:
            self.velocity += GRAVITY
            self.rect.y += self.velocity
            if self.rect.y > HEIGHT - self.rect.height:
                self.rect.y = HEIGHT - self.rect.height
                self.velocity = 0

    def jump(self):
        if self.rect.y == HEIGHT - self.rect.height:
            self.velocity = -10

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.is_ragdoll = True

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Collision detection
def check_collision(player1, player2):
    return player1.rect.colliderect(player2.rect)

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ragdoll Fighter")
    clock = pygame.time.Clock()

    player1 = Player(100, HEIGHT - 50)
    player2 = Player(600, HEIGHT - 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        player1.update()
        player2.update()

        # Check collisions
        if check_collision(player1, player2):
            player1.take_damage(1)
            player2.take_damage(1)

        # Draw
        screen.fill((0, 0, 0))
        player1.draw(screen)
        player2.draw(screen)

        # Health bars
        pygame.draw.rect(screen, RED, (10, 10, player1.health * 2, 20))
        pygame.draw.rect(screen, RED, (WIDTH - player2.health * 2 - 10, 10, player2.health * 2, 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()