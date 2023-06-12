import pygame
import math

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Motion in Circle with Reflection and Rotation")

# Load ball image
ball_image = pygame.image.load("ball.png")
ball_image = pygame.transform.scale(ball_image, (50, 50))  # Resize image
ball_rect = ball_image.get_rect()

# Circle parameters
circle_center = (width // 2, height // 2)
circle_radius = 200

# Ball parameters
ball_radius = ball_rect.width // 2
ball_angle = 0
ball_rotation_angle = 0
ball_rotation_speed = 2

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill('green')
    
    # Draw the circle
    pygame.draw.circle(screen, 'blue', circle_center, circle_radius, 10)

    # Calculate the ball's position on the circle
    ball_angle -= ball_rotation_speed
    ball_angle %= 360
    ball_position_x = circle_center[0] + math.cos(math.radians(ball_angle)) * (circle_radius - ball_radius)
    ball_position_y = circle_center[1] + math.sin(math.radians(ball_angle)) * (circle_radius - ball_radius)

    # Rotate the ball image
    rotated_image = pygame.transform.rotate(ball_image, ball_rotation_angle)
    rotated_rect = rotated_image.get_rect(center=ball_rect.center)

    # Blit the rotated ball image onto the screen at the ball's position
    rotated_rect.center = (ball_position_x, ball_position_y)
    screen.blit(rotated_image, rotated_rect)

    # Update the rotation angle for the ball
    ball_rotation_angle += ball_rotation_speed*3
    ball_rotation_angle %= 360

    # Update the display
    pygame.display.flip()

    # Control the game's frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
