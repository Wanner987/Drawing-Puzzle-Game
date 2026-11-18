import pygame

class DrawingSurface:
    def __init__(self,
        targetSurface : pygame.Surface, 
        size : tuple[int, int] = (500, 500),
        position : tuple[int, int] = (0,0)
    ):
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.targetSurface = targetSurface
        self.position = position

    def clear(self):
        self.surface.fill((255, 255, 255))

    def draw(self):
        self.targetSurface.blit(self.surface, self.position)
    
    def outline(self):
        pygame.draw.rect(
            self.surface,
            (255, 0, 0),          # Border color
            self.surface.get_rect(),   # Rectangle dimensions
            width=3               # Border thickness
        )

