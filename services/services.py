import random
from lexicon.lexicon_ru import JEST

def random_jest (answer):
    computer_answer = random.choice(list(JEST.keys()))
    if answer == computer_answer:
        return "Ничья", computer_answer
    if JEST[answer] == computer_answer:
        return "Ты победил", computer_answer
    return "Я победил", computer_answer
