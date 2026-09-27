import pygame
from .Scenes import Scene
from app.Elements.Scenes.StartingScreen import StartingScreen

class SceneManager:
    def __init__(self, initScene : str, screen: pygame.Surface):
        self.SCREEN = screen


        self.all_scenes = [
            StartingScreen(self.SCREEN)
        ]
        self.SCENES = self.get_all_scenes()

        # start the init scene
        if initScene not in self.SCENES:
            raise KeyError("Initial scene could not be found")
        else:
            self.CURRENT_SCENE : Scene = self.SCENES[initScene]

        self.CURRENT_SCENE.enter()

    def get_all_scenes(self):
        myDict = {}

        for scene in self.all_scenes:
            myDict[scene.NAME] = scene
        
        return myDict

    def change_scene(self, current_scene, new_scene = "default"):
        new_scene = self.SCENES.get(new_scene.lower())

        if new_scene is None:
            raise KeyError("New Scene could not be found")
        
        self.CURRENT_SCENE.exit()
        self.CURRENT_SCENE = new_scene
        self.CURRENT_SCENE.enter()

    def update(self):
        self.CURRENT_SCENE.update()

    def get_screen(self):
        return self.SCREEN