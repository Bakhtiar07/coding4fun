import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.RESIZABLE, vsync=1 )
pygame.display.set_caption('Pong')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle properties
paddle_width, paddle_height = 10, 60
left_paddle_speed = 0
right_paddle_speed = 0
paddle_speed = 6

# Ball properties
ball_width, ball_height = 10, 10
ball_x_speed = 4
ball_y_speed = 4

# Initial positions
left_paddle_x = 10
left_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2
right_paddle_x = SCREEN_WIDTH - 10 - paddle_width
right_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2
ball_x = SCREEN_WIDTH // 2 - ball_width // 2
ball_y = SCREEN_HEIGHT // 2 - ball_height // 2

# Clock for controlling the frame rate
clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle_speed = -paddle_speed
            if event.key == pygame.K_s:
                left_paddle_speed = paddle_speed
            if event.key == pygame.K_UP:
                right_paddle_speed = -paddle_speed
            if event.key == pygame.K_DOWN:
                right_paddle_speed = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                left_paddle_speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                right_paddle_speed = 0

    # Move paddles
    left_paddle_y += left_paddle_speed
    right_paddle_y += right_paddle_speed

    # Prevent paddles from going out of bounds
    left_paddle_y = max(left_paddle_y, 0)
    left_paddle_y = min(left_paddle_y, SCREEN_HEIGHT - paddle_height)
    right_paddle_y = max(right_paddle_y, 0)
    right_paddle_y = min(right_paddle_y, SCREEN_HEIGHT - paddle_height)

    # Move ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Collision detection with walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - ball_height:
        ball_y_speed *= -1
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_width:
        ball_x_speed *= -1  # Reset ball position or update score here for a real game

    # Collision detection with paddles
    if (ball_x <= left_paddle_x + paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height) or \
       (ball_x + ball_width >= right_paddle_x and right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_x_speed *= -1

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_width, ball_height))

    # Updating the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)/1000
