import pygame
from .Scenes import Scene


class SceneManager:
    def __init__(self, initScene, screen):
        self.SCREEN = screen
        self.SCNENES = self.get_all_scenes()

        if not isinstance(initScene, Scene):
            raise TypeError("Must give Scene object as the init")
        else:
            self.CURRENT_SCENE = initScene

        initScene.enter()

    def get_all_scenes(self):
        
        
        return {
            "default": Scene()
        }

    def change_scene(self, current_scene, new_scene):
        pass

    def update(self):
        self.CURRENT_SCENE.update()

    def get_screen(self):
        return self.SCREEN