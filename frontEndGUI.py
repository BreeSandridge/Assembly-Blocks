from arcade.GUI import *
import os

import arcade

arcade.set_background_color(arcade.color.WHITE)


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = "System Instructions"
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def setup(self):
        self.text_list.append(arcade.TextLabel(self.center_x - 225, self.center_y))
        self.textbox_list.append(arcade.TextBox(self.center_x - 125, self.center_y))
        self.button_list.append(arcade.SubmitButton(self.textbox_list[0], self.on_submit,
                                                    self.center_x,
                                                    self.center_y))


class Halt(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="halt", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Read(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="read", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Write(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="write", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Nop(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="nop", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = "Setting Register Data"
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def setup(self):
        self.text_list.append(arcade.TextLabel(self.center_x - 225, self.center_y))
        self.textbox_list.append(arcade.TextBox(self.center_x - 125, self.center_y))
        self.button_list.append(arcade.SubmitButton(self.textbox_list[0], self.on_submit,
                                                    self.center_x,
                                                    self.center_y))


class Setn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="setn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class  Addn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="addn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Copy(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="copy", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = "Arithmetic"
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def setup(self):
        self.text_list.append(arcade.TextLabel(self.center_x - 225, self.center_y))
        self.textbox_list.append(arcade.TextBox(self.center_x - 125, self.center_y))
        self.button_list.append(arcade.SubmitButton(self.textbox_list[0], self.on_submit,
                                                    self.center_x,
                                                    self.center_y))


class Add(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="add", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Neg(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="neg", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Mul(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="mul", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Div(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="div", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Mod(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="mod", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = "Interacting with Memory"
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def setup(self):
        self.text_list.append(arcade.TextLabel(self.center_x - 225, self.center_y))
        self.textbox_list.append(arcade.TextBox(self.center_x - 125, self.center_y))
        self.button_list.append(arcade.SubmitButton(self.textbox_list[0], self.on_submit,
                                                    self.center_x,
                                                    self.center_y))


class Loadn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="loadn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Storen(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="storen", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Loadr(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="loadr", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Storer(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="storer", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = "Jump"
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def setup(self):
        self.text_list.append(arcade.TextLabel(self.center_x - 225, self.center_y))
        self.textbox_list.append(arcade.TextBox(self.center_x - 125, self.center_y))
        self.button_list.append(arcade.SubmitButton(self.textbox_list[0], self.on_submit,
                                                    self.center_x,
                                                    self.center_y))

class Jumpn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jumpn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jumpr(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jumpr", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jeqzn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jeqzn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jnezn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jnezn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jgtzn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jgtzn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jltzn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jltzn", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Calln(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="calln", theme=None):
        super().__init__(x, y, width, height, text, theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False