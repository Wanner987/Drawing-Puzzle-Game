import pygame

class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.drawingArea = None  # This will be set to a pygame.Rect defining the drawing area
        self.shapes = []
        self.color = (0, 0, 0)  # Default color is black // will change later

    def start_draw(self):
        pass

    def draw_process(self):
        mouse_pos = pygame.mouse.get_pos()
        

    def end_draw(self, vectors):
        self.shapes.append(vectors)
    
