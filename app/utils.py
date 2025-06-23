import random
from random import randint

from text import vocabulary


def game_step():
    truth, *lei = random.sample(list(vocabulary.keys()), 5)
    lei[randint(0, 3)] = truth
    return truth, vocabulary[truth], lei