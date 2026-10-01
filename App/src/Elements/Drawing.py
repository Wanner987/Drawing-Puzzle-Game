import pygame

class Drawing:
    def __init__(self, screen, penSize=5):
        self.screen : pygame.Surface = screen
        self.drawingArea = None  # This will be set to a pygame.Rect defining the drawing area
        self.shapes = []
        self.color = (0, 0, 0)  # Default color is black // will change later
        self.penSize = penSize

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, self.color, mouse_pos, self.penSize)
    
