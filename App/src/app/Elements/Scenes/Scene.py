import pygame
from ..SceneManager import SceneManager

class Scene:
    def __init__(self):
        self.SCRENE = SceneManager.get_screen

    def enter(self):
        pass

    def update(self):
        raise NotImplementedError("Must have a process")

    def exit(self):
        pass
