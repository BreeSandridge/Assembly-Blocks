import arcade
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "LEGOS"
BLOCK_QUANTITIY = 10


class MyGame(arcade.Window):
    def __init__(self):
        super.__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.set_mouse_visible(True)
        blockList = [NewBlocks(self, 300, 610 - 20*i) for i in range(20)]

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        isPressing = False

    #def on_draw(self):
     #   """ Render the screen. """

        #arcade.start_render()
        # Code to draw the screen goes here

    def dragBlocks(self, x, y, dx, dy, button):
        arcade.Window.on_mouse_drag(x, y, dx, dy, button)

    def automaticClick(self, button_dragged, button_static):
        distance = ((button_dragged.x - button_static.x)**2+(button_dragged.y - button_static.y)**2)**2.0
        maxClickingDistance = 5
        if distance < maxClickingDistance:
            if button_dragged.y < button_static.y-button_static.height:
                button_dragged.position_x = button_static.x
                button_dragged.position_y = button_static.y-button_static.height+1
            if button_dragged.y > button_static.y-button_static.height:
                button_dragged.position_x = button_static.x
                button_dragged.position_y = button_static.y+button_static.height-1

    def on_mouse_motion(self, button, x, y, dx, dy):
        button.position_x = x
        button.position_y = y




def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()





class Blocks:
    def __init__(self,
                 center_x, center_y, width, height, text, font_size=18,
                 font_face="Arial"):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.isPressed = False
        self.above = center_y+(self.height/2)
        self.below = center_y-(self.height/2)

        def draw(self):
            """ Draw the button """
            arcade.draw_rectangle_filled(self.above, self.center_y, self.width,
                                         self.height, self.face_color)


        arcade.draw_text(self.text, self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

class NewBlocks(Blocks):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, 10, 60, 18, "Arial")