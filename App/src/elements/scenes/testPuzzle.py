from .scene import Scene

class TestPuzzle(Scene):
    def __init__(self, screen, name = "default"):
        super().__init__(screen, name)

    def enter(self):
        return super().enter()

    def update(self):
        return super().update()

    def exit(self):
        return super().exit()