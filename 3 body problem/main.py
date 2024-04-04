import pygame
from math import sqrt

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600  # Increased height for better visibility
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3-Body Problem Simulation: Proportional Planet Size")

# Define colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue for different planets

# Planet class to hold information about the planets
class Planet:
    def __init__(self, mass, position, color):
        self.mass = mass
        self.position = position
        self.velocity = [0, 0]
        self.color = color  # Assigned color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), int(self.mass))

# Function to calculate gravitational force
def calculate_gravitational_force(planet1, planet2):
    G = 6.67430  # Gravitational constant
    min_distance = 20  # Minimum distance to prevent 'explosions'
    distance_x = planet2.position[0] - planet1.position[0]
    distance_y = planet2.position[1] - planet1.position[1]
    distance = sqrt(distance_x**2 + distance_y**2)
    distance = max(distance, min_distance)  # Prevent division by zero and explosions

    force = G * planet1.mass * planet2.mass / distance**2
    force_x = force * distance_x / distance
    force_y = force * distance_y / distance

    return force_x, force_y

# Main loop

running = True
planets = []
clicks = 0
time_step = 0.1
available_colors = colors.copy()
mouse_down_time = None
paused = False #Add a pause variable

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and clicks < 3:
                mouse_down_time = pygame.time.get_ticks()
                
            if event.type == pygame.MOUSEBUTTONUP and clicks < 3 and mouse_down_time is not None:
                mouse_up_time = pygame.time.get_ticks()
                mass = (mouse_up_time - mouse_down_time) / 20  # Adjust size based on click duration
                position = pygame.mouse.get_pos()
                color = available_colors.pop(0) if available_colors else (255, 255, 255)  # Default to white if out of colors
                planets.append(Planet(mass, list(position), color))
                clicks += 1
                # Draw the planet immediately on click
                planets[-1].draw(screen)
                pygame.display.flip()
                mouse_down_time = None

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                planets = []
                clicks = 0
                available_colors = colors.copy()
                screen.fill((0, 0, 0))
                pygame.display.flip()
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused # Toggle pause state
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()

        if clicks >= 3 and not paused: 
            # Update planet positions based on gravitational forces
            for i, planet1 in enumerate(planets):
                total_fx = total_fy = 0
                for j, planet2 in enumerate(planets):
                    if i != j:
                        fx, fy = calculate_gravitational_force(planet1, planet2)
                        total_fx += fx
                        total_fy += fy

                # Update velocities
                planet1.velocity[0] += total_fx / planet1.mass * time_step
                planet1.velocity[1] += total_fy / planet1.mass * time_step

                # Update positions
                planet1.position[0] += planet1.velocity[0] * time_step
                planet1.position[1] += planet1.velocity[1] * time_step

            # Draw planets without clearing the screen to keep trails
            for planet in planets:
                planet.draw(screen)

            pygame.display.flip()

pygame.quit()
