from arcade.GUI import *
import os

class Halt(TextButton):
    def __init__(self, game, x = 0, y = 0, width = 100, height = 40, text = "Halt", theme = None):
        super().__init__(x, y, width, height, text, theme = theme)
        self.game = game
    def on_press(self):
        self.pressed = True
    def on_release(self):
        if self.pressed:
            self.pressed = False

