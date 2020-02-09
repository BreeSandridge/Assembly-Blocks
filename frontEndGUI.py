from arcade.GUI import *
import os

import arcade

arcade.set_background_color(arcade.color.WHITE)


class SystemInstructions(arcade.Window):
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
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Read(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="read", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Write(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="write", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Nop(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="nop", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class SettingRegisterData(arcade.Window):
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
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Addn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="addn", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Copy(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="copy", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Arithmetic(arcade.Window):
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
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Sub(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="sub", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Neg(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="neg", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Mul(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="mul", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Div(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="div", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Mod(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="mod", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
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
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Storen(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="storen", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Loadr(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="loadr", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Storer(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="storer", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jumps(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = "Jumps"
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
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jumpr(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jumpr", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jeqzn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jeqzn", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jnezn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jnezn", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jgtzn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jgtzn", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Jltzn(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="jltzn", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class Calln(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="calln", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False


class AssemblyBlock(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Assembly Blocks")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.AMAZON)
        self.pause = False
        self.text = "Welcome To Assembly Blocks"
        self.text_x = 0
        self.text_y = 300
        self.text_font_size = 40
        self.speed = 1
        self.theme = None

    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.theme = Theme()
        self.theme.set_font(24, arcade.color.WHITE)
        self.set_button_textures()

    def set_buttons(self):
        self.button_list.append(Setn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Addn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Copy(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Add(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Sub(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Neg(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Mul(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Div(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Mod(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Loadn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Storen(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Loadr(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Storer(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Jumpn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Jumpr(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Jeqzn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Jnezn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Jgtzn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Jltzn(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(Calln(self, 60, 570, 110, 50, theme=self.theme))

    def setup(self):
        self.setup_theme()
        self.set_buttons()

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        arcade.draw_text(self.text, self.text_x, self.text_y, arcade.color.ALICE_BLUE, self.text_font_size)


def main():
    game = AssemblyBlock()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
