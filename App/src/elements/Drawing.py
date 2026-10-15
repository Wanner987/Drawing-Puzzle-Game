import pygame
from .recognizeDrawing import recognizeDrawing

class Drawing:
    def __init__(self, screen, penSize=5):
        self.screen : pygame.Surface = screen
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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._drawPoints = []
        self.draw()

        if event.type == pygame.MOUSEBUTTONUP:
            self.end_draw()
    
    def draw(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            self._drawPoints.append(mouse_pos)

            # Display what is drawn
            pygame.draw.circle(self.screen, self.color, mouse_pos, self.penSize)

    def end_draw(self):
        if not self._is_recognizing:
            return
        
        recognizer = recognizeDrawing()
        resample = recognizer.resample_points(self._drawPoints)
        recognizer.recognize(resample)