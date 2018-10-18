# Your name goes here :)
from aluLib import *

# I'm providing you with a general structure, but feel free to remove ALL
# OF IT and do it your way

CARD_WIDTH = 100
CARD_HEIGHT = 145
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# You will probably still need quite a few globals
cards = ['A', 'A', 'K', '2', '2', 'K']

# This function will draw the cards
def draw_cards():
    # remove the line below once you start working on this
    pass

# This function decides what should happen given the state of the cards
# Are there any cards we should remove? any cards we should hide?
# You won't need this until milestone 3
def check_card_state():
    # remove the line below once you start working on this
    pass

# Check the mouse input, and flip relevant cards
def check_mouse_input():
    # remove the line below once you start working on this
    pass

def main():
    # As mentioned, this is just a suggested structure. Feel free to change this if you prefer
    clear()
    draw_cards()
    check_card_state()
    check_mouse_input()


# Keep a low framerate to your submission. 10 worked well for me, but experiment on your own.
start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=10)
