
import pygame
from math import sqrt

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3-Body Problem Simulation with Fixed Mass Display")

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

# Function to draw planet masses in a fixed position on the screen
def draw_masses_in_fixed_position(screen, planets):
    font = pygame.font.Font(None, 24)
    starting_y = 20  # Starting y position for the first mass display
    for i, planet in enumerate(planets):
        mass_text = "Mass of Planet {}: {:.2f}".format(i+1, planet.mass)
        text_surface = font.render(mass_text, True, planet.color)
        screen.blit(text_surface, (20, starting_y + i*30))  # Display each mass 30 pixels apart

# Main loop
def main():
    running = True
    planets = []
    clicks = 0
    time_step = 0.1
    available_colors = colors.copy()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and clicks < 3:
                mouse_down_time = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONUP and clicks < 3:
                mouse_up_time = pygame.time.get_ticks()
                mass = (mouse_up_time - mouse_down_time) / 10
                position = pygame.mouse.get_pos()
                color = available_colors.pop()
                planets.append(Planet(mass, list(position), color))
                clicks += 1
                screen.fill((0, 0, 0))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                planets = []
                clicks = 0
                available_colors = colors.copy()
                screen.fill((0, 0, 0))
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()

        if clicks >= 1:  # Draw fixed masses as soon as the first planet is created
            screen.fill((0, 0, 0))  # Clear screen to avoid trails
            draw_masses_in_fixed_position(screen, planets)

        if clicks == 3:
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

            # Draw planets
            for planet in planets:
                planet.draw(screen)

        pygame.display.flip()

# Run the simulation
if __name__ == "__main__":
    main()
