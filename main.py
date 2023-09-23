import random

SUITS = (
    "♠",
    "♥",
    "♦",
    "♣",
)
RANKS = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A"
)


class Card:
    pass


class Deck:
    cards = []

    def __init__(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(f"{rank}{suit}")

    def shuffle(self):
        return random.shuffle(self.cards)


if __name__ == "__main__":
    print("Hi Caravan!")
    deck = Deck()
    print(deck.cards)
    deck.shuffle()
    print(deck.cards)
