import pygame
from .Scene import Scene
from ..SceneManager import SceneManager

class StartingScreen(Scene):
    def __init__(self):
        super().__init__()

    def enter(self):
        pass

    def update(self):
        raise NotImplementedError("Must have a process")

    def exit(self):
        pass
