import pygame
from .recognizeDrawing import recognizeDrawing
from .drawingSurface import DrawingSurface

class Drawing:
    def __init__(self, drawingSurface : DrawingSurface, penSize=5):
        self.drawingSurface = drawingSurface
        self.surface = drawingSurface.surface
        self.drawingArea = None  # This will be set to a pygame.Rect defining the drawing area
        self.color = (0, 0, 0)  # Default color is black // will change later
        self.penSize = penSize
        self._drawPoints = []
        self._is_drawing : bool = True
        self._is_recognizing : bool = True

    def activateRecognition(self):
        self._is_recognizing = True

    def deactivateRecognition(self):
        self._is_recognizing = False

    def activateDrawing(self):
        self._is_drawing = True

    def deactivateDrawing(self):
        self._is_drawing = False
    
    def drawUpdate(self, event : pygame.event):
        if not self._is_drawing:
            return

        # Reset the draw points when the mouse is first pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.surface.get_rect(topleft=self.drawingSurface.position).collidepoint(mouse_pos):
                self._drawPoints = []
        
        # While left mouse is down and in surface area draw
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.surface.get_rect(topleft=self.drawingSurface.position).collidepoint(mouse_pos):
                self.draw()

        # Recognize drawing when mouse is lifted
        if event.type == pygame.MOUSEBUTTONUP:
            self.end_draw()
    
    def draw(self):
        screen_pos = self.drawingSurface.position
        mouse_pos = pygame.mouse.get_pos()
        draw_position = (
            mouse_pos[0] - screen_pos[0],
            mouse_pos[1] - screen_pos[1]
        )
        self._drawPoints.append(mouse_pos)

        # Display what is drawn
        pygame.draw.circle(self.surface, self.color, draw_position, self.penSize)

    def end_draw(self):
        if not self._is_recognizing:
            return
        
        recognizer = recognizeDrawing()
        resample = recognizer.resample_points(self._drawPoints)
        recognizer.recognize(resample)