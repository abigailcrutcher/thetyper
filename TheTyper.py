import arcade
"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class TheGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height):
        super().__init__(width, height, title="The Typer")


    def setup(self):
        """ Set up the game and initialize the variables. """


    def update(self, dt):
        """ Move everything """


    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()


    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        print(key)



def main():
    window = TheGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()