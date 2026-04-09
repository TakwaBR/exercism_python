"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    baking_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time

    return baking_time_remaining


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers of your lasagna.
    :return: int - Time you spend to make all the layers.

    Function that takes the number of layers you want to put in your lasagna
    and returns how many minutes the it takes to make all the layers.
    """
    making_all_layers = PREPARATION_TIME * number_of_layers

    return making_all_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time spend in kitchen.

    :param number_of_layers: int - number of layers of your lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - Time you spend in the kitchen.

    Function that takes the number of layers in your lasagna and
    the time the lasagna has spent baking
    and returns how many minutes you spend in the kitchen.
    """
    preparation_time_layering = preparation_time_in_minutes(number_of_layers)
    time_spend_in_kitchen = preparation_time_layering + elapsed_bake_time

    return time_spend_in_kitchen
