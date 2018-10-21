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
horiz_space_between_cards = (WINDOW_WIDTH - (len(cards) * CARD_WIDTH)) / (len(cards) + 1)
vert_space_between_cards = (WINDOW_HEIGHT - 2) / 3

# This function will draw the cards
def draw_cards():

    count = 0
    card_x = horiz_space_between_cards
    card_y = vert_space_between_cards

    while count < len(cards):
        img = load_image("assets/" + cards[count] + ".png")
        draw_image(img, card_x, card_y)
        card_x += CARD_WIDTH + horiz_space_between_cards

        count += 1


# This function decides what should happen given the state of the cards
# Are there any cards we should remove? any cards we should hide?
# You won't need this until milestone 3
def check_card_state():
    # remove the line below once you start working on this
    pass

# Check the mouse input, and flip relevant cards
def check_mouse_input():
    if is_mouse_pressed():
        clicked_point_x = mouse_x()
        clicked_point_y = mouse_y()
        # if is_mouse_on_card(clicked_point_x, clicked_point_y):
        #     print(get_value_and_index(clicked_point_x, clicked_point_y))


def is_mouse_on_card(x, y):
    if not(horiz_space_between_cards <= x <= WINDOW_WIDTH - horiz_space_between_cards or
           vert_space_between_cards <= y <= WINDOW_HEIGHT - vert_space_between_cards):
            return False

    count = 1
    while count < len(cards) + 1:
        if horiz_space_between_cards * count + CARD_WIDTH * (count - 1) <= x <= (horiz_space_between_cards + CARD_WIDTH) * count:
            if vert_space_between_cards <= y <= vert_space_between_cards + CARD_HEIGHT or \
                   WINDOW_HEIGHT - vert_space_between_cards - CARD_HEIGHT <= y <= WINDOW_HEIGHT - vert_space_between_cards:
                return True
        count += 1
    return False




def main():
    # As mentioned, this is just a suggested structure. Feel free to change this if you prefer
    clear()
    draw_cards()
    check_card_state()
    check_mouse_input()


# Keep a low framerate to your submission. 10 worked well for me, but experiment on your own.
start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=10)
