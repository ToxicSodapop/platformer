import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("My Platformer Game")

# Define a Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 50])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 400
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# Define a Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

# Create groups for all sprites and all platforms
all_sprites_group = pygame.sprite.Group()
all_platforms_group = pygame.sprite.Group()

# Create the player and add it to the all_sprites_group
player = Player()
all_sprites_group.add(player)

# Create some platforms and add them to the all_sprites_group and all_platforms_group
for i in range(10):
    platform = Platform(random.randint(50, 100), 20)
    platform.rect.x = random.randint(0, SCREEN_WIDTH - platform.rect.width)
    platform.rect.y = random.randint(0, SCREEN_HEIGHT - platform.rect.height)
    all_sprites_group.add(platform)
    all_platforms_group.add(platform)

# Set up the game loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -5
            elif event.key == pygame.K_RIGHT:
                player.change_x = 5
            elif event.key == pygame.K_SPACE:
                player.change_y = -10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.change_x = 0

    # Update the player and all platforms
    all_sprites_group.update()

    # Check for collisions between the player and the platforms
    platform_collisions = pygame.sprite.spritecollide(player, all_platforms_group, False)
    # If there is a collision, move the player back to the top of the platform
    for platform in platform_collisions:
        if player.rect.bottom < platform.rect.bottom:
            player.rect.bottom = platform.rect.top
            player.change_y = 0

    # Fill the background with black
    screen.fill(BLACK)

    # Draw all sprites to the screen
    all_sprites_group.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 60 fps
    clock.tick(60)

# Quit the game
pygame.quit()
