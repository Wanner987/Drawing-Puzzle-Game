
import pygame


class PhysicsObject:
    def __init__(
        self,
        position: tuple[float, float],
        mass: float = 1.0,
        velocity: tuple[float, float] = (0, 0),
    ):
        # Physical properties
        self.mass = mass

        # Motion properties
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.acceleration = pygame.Vector2(0, 0)

        # Rendering properties
        self.radius = 15
        self.color = (255, 0, 0)

    def apply_force(self, force: pygame.Vector2):
        """Apply a force to the object using F = ma."""
        self.acceleration += force / self.mass

    def update(self, delta_time: float):
        """Update the object's physics."""

        # Update velocity using acceleration
        self.velocity += self.acceleration * delta_time

        # Update position using velocity
        self.position += self.velocity * delta_time

        # Reset acceleration after each physics update
        self.acceleration.update(0, 0)

    def draw(self, screen: pygame.Surface):
        """Draw the object."""
        pygame.draw.circle(
            screen,
            self.color,
            self.position,
            self.radius
        )
