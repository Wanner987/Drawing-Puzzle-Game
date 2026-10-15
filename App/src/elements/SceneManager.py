import pygame
from .scenes.scene import Scene
from .eventManager import EventManager
from collections import deque

# Scenes
from elements.scenes.startingScreen import StartingScreen
from elements.scenes.testScene import TestScene
from elements.scenes.testPuzzle import TestPuzzle


class SceneManager:
    def __init__(self, initScene : str, screen: pygame.Surface):
        self.SCREEN = screen

        # put all scenes here
        self.all_scenes = [
            StartingScreen(self.SCREEN, "startingScreen"),
            TestScene(self.SCREEN, "testScene"),
            TestPuzzle(self.SCREEN, "testPuzzle")
        ]

        # Dict with SceneName : SceneObject
        self.SCENES = self.get_all_scenes()

        # Add change scene to event manager
        EventManager.onSceneChange.append(self.change_scene)

        # start the init scene
        if initScene not in self.SCENES:
            raise KeyError("Initial scene could not be found")
        
        self.CURRENT_SCENE : Scene = self.SCENES[initScene]

        self.CURRENT_SCENE.enter()

    def get_all_scenes(self):
        # Testing importing from scenes recurisvely so I don't have to add them to the list above 
        # 
        # queue = deque(Scene.__subclasses__())
        # seen = set()

        # while queue:
        #     subclass = queue.popleft()
        #     if subclass not in seen:
        #         seen.add(subclass)
        #         # Add further generations to the queue
        #         queue.extend(subclass.__subclasses__())
                
        # print(seen)
        
        
        myDict = {}

        for scene in self.all_scenes:
            myDict[scene.NAME] = scene
        
        return myDict

    def change_scene(self, current_scene : Scene, new_scene = "default"): # change default to errorScene
        new_scene = self.SCENES.get(new_scene)

        if new_scene is None:
            raise KeyError("New Scene could not be found")

        if current_scene is not self.CURRENT_SCENE:
            raise KeyError("Current scene provided does not match the current scene in the manager")
        
        current_scene.exit()
        current_scene = new_scene
        current_scene.enter()

        self.CURRENT_SCENE = current_scene

    def update(self):
        self.CURRENT_SCENE.update()

    def get_screen(self):
        return self.SCREEN