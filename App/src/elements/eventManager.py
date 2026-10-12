class EventManager:
    
    onQuitGame : list = []

    @classmethod
    def quitGame(cls):
        if len(cls.onQuitGame) != 0:
            for function in cls.onQuitGame:
                function()

    onSceneChange : list = []
    @classmethod
    def changeScene(cls, currentScene, nextScene):
        if len(cls.onSceneChange):
            for function in cls.onSceneChange:
                function(currentScene, nextScene)
    
    onShapeRecognized : list = []
    @classmethod
    def shapeRecognized(cls, shape : str):
        if len(cls.onShapeRecognized) > 0:
            for func in cls.onShapeRecognized:
                func(shape)
    
    # 