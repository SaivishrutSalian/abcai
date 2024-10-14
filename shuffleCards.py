import random

types = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q', 'K', 'A']

deck = [f'{rank} of {t}' for rank in ranks for t in types]

random.shuffle(deck)
for card in deck:
    print(card)

