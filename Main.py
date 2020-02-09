import arcade
import random
import os
import GuiInteraction

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "hjgjh"


class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height
        self.visible = False

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()


class Instructions(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "System Instructions", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Data(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Setting Register Data", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Arithmetic(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Arithmetic", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jumps(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Jumps", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Memory(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Interacting with Memory", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Halt(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "halt", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Read(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "read", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Write(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "write", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Nop(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "nop", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Setn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Setn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Addn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "addn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Copy(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "copy", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Add(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "add", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Sub(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "sub", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Neg(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "neg", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Mul(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "mul", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Div(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "div", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Mod(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "mod", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jumpn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "jumpn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jumpr(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "jumpr", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jeqzn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "jeqzn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jnezn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "jnezn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jgtzn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "jgtzn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Jltzn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "jltzn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Calln(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "calln", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Loadn(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "loadn", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Storen(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "storen", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Loadr(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "loadr", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Storer(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "storer", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Create our on-screen GUI buttons
        self.button_list = []

        # def on_draw_inital_buttons(self):
        # arcade.start_render()
        instructions = Instructions((.5 * SCREEN_WIDTH), (SCREEN_HEIGHT - 30), self.resume_program)
        self.button_list.append(instructions)
        # instructions.draw()
        data = Data((.5 * SCREEN_WIDTH), (SCREEN_HEIGHT - 80), self.resume_program)
        self.button_list.append(data)
        # data.draw()
        arithmetic = Arithmetic((.5 * SCREEN_WIDTH), (SCREEN_HEIGHT - 130), self.resume_program)
        self.button_list.append(arithmetic)
        # arithmetic.draw()
        jumps = Jumps((.5 * SCREEN_WIDTH), (SCREEN_HEIGHT - 180), self.resume_program)
        self.button_list.append(jumps)
        # jumps.draw()
        memory = Memory((.5 * SCREEN_WIDTH), (SCREEN_HEIGHT - 230), self.resume_program)
        self.button_list.append(memory)
        # memory.draw()
    def on_draw_inital_buttons(self):
        arcade.start_render()
        for button in self.button_list:
            button.draw()

        if Instructions.pressed:
            instructions.visible = True
            halt = Halt(60, 570, self.resume_program)
            self.button_list.append(halt)
            read = Read(60, 570, self.resume_program)
            self.button_list.append(read)
            write = Write(60, 570, self.resume_program)
            self.button_list.append(write)
            nop = Nop(60, 570, self.resume_program)
            self.button_list.append(nop)

        if Data.pressed:
            data.visible = True
            setn = Setn(60, 570, self.resume_program)
            self.button_list.append(setn)
            addn = Addn(60, 570, self.resume_program)
            self.button_list.append(addn)
            copy = Copy(60, 570, self.resume_program)
            self.button_list.append(copy)

        if Arithmetic.pressed:
            arithmetic.visible = True
            add = Add(60, 570, self.resume_program)
            self.button_list.append(add)
            sub = Sub(60, 570, self.resume_program)
            self.button_list.append(sub)
            neg = Neg(60, 570, self.resume_program)
            self.button_list.append(neg)
            mul = Mul(60, 570, self.resume_program)
            self.button_list.append(mul)
            div = Div(60, 570, self.resume_program)
            self.button_list.append(div)
            mod = Mod(60, 570, self.resume_program)
            self.button_list.append(mod)

        if Jumps.pressed:
            jumps.visible = True
            jumpn = Jumpn(60, 570, self.resume_program)
            self.button_list.append(jumpn)
            jumpr = Jumpr(60, 570, self.resume_program)
            self.button_list.append(jumpr)
            jeqzn = Jeqzn(60, 570, self.resume_program)
            self.button_list.append(jeqzn)
            jnezn = Jnezn(60, 570, self.resume_program)
            self.button_list.append(jnezn)
            jgtzn = Jgtzn(60, 570, self.resume_program)
            self.button_list.append(jgtzn)
            jltzn = Jltzn(60, 570, self.resume_program)
            self.button_list.append(jltzn)
            calln = Calln(60, 570, self.resume_program)
            self.button_list.append(calln)

        if Memory.pressed:
            memory.visible = True
            loadn = Loadn(60, 570, self.resume_program)
            self.button_list.append(loadn)
            storen = Storen(60, 570, self.resume_program)
            self.button_list.append(storen)
            loadr = Loadr(60, 570, self.resume_program)
            self.button_list.append(loadr)
            storer = Storer(60, 570, self.resume_program)
            self.button_list.append(storer)


    def on_draw_instructions(self):
        arcade.start_render()
        for button in self.button_list:
            if instructions.visible:
              button.draw()

    def on_draw_data(self):
        arcade.start_render()
        for button in self.button_list:
            if data.visible:
              button.draw()

    def on_draw_arithmetic(self):
        arcade.start_render()
        for button in self.button_list:
            if arithmetic.visible:
              button.draw()

    def on_draw_jumps(self):
        arcade.start_render()
        for button in self.button_list:
            if jumps.visible:
              button.draw()

    def on_draw_memory(self):
        arcade.start_render()
        for button in self.button_list:
            if memory.visible:
              button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)


    def resume_program(self):
        self.pause = False


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()