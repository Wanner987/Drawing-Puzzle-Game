import pygame
from .scene import Scene
from ..config import Config
from ..physics.physicsObject import PhysicsObject
from ..drawing.drawing import Drawing
from ..eventManager import EventManager
from ..drawing.drawingSurface import DrawingSurface

class TestPuzzle(Scene):
    def __init__(self, screen, name = "default"):
        super().__init__(screen, name)

    def enter(self):
        self.SCREEN.fill("white")
        self.drawingSurface = DrawingSurface(self.SCREEN, (500,500), (100, 100))
        self.drawing = Drawing(self.drawingSurface, 10)
        self.physicsObject = PhysicsObject((100, 100), 1, (0,0))
        EventManager.onShapeRecognized.append(self.moveObject)

    def update(self, delta=0):
        self.SCREEN.fill((255, 255, 255))
        self.drawingSurface.draw()
        self.drawingSurface.outline()
        physicsObject = self.physicsObject
        for event in pygame.event.get():
            self.drawing.drawUpdate(event)
        
        physicsObject.update(delta)
        physicsObject.draw(self.SCREEN)

        

    def exit(self):
        EventManager.onShapeRecognized.remove(self.moveObject)

    def moveObject(self, shape : str):
        physicsObject = self.physicsObject
        movement = {
            "line-up": lambda: physicsObject.apply_force(pygame.Vector2(0.0, -500.0)),     
            "line-down": lambda: physicsObject.apply_force(pygame.Vector2(0.0, 500.0)),       
            "line-left": lambda: physicsObject.apply_force(pygame.Vector2(-500.0, 0.0)),      
            "line-right": lambda: physicsObject.apply_force(pygame.Vector2(500.0, 0.0)),  
            "u-up": None,       
            "u-down": None,          
            "u-left": None,    
            "u-right": None,   
        }

        movement = movement.get(shape.lower())

        if movement is not None:
            self.drawingSurface.clear()
            movement()