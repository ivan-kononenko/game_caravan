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


class Player:
    hand = []

    def __init__(self):
        self.deck = Deck

    def give_hand(self):
        self.hand.append(self.deck.cards[:8])
        return self.hand


class Card:
    value = None
    holder = None

    def __init__(self, value, holder="deck"):
        self.value = value
        self.holder = holder

    def __str__(self):
        return f"{self.value} at {self.holder}"


class Deck:
    cards = []

    def __init__(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(f"{rank}{suit}"))
        self.cards.append(Card("RJ"))
        self.cards.append(Card("BJ"))

    def shuffle(self):
        return random.shuffle(self.cards)

    def __str__(self):
        #list amount of cards currently in deck
        return f"Deck currently has {len(self.cards)} cards."

    def deal(self, holder):
        #receives list of players(p1, p2 and so on) and amount of card to give out to each player. Assign cards to player
        return f"{self.value} at {self.holder}"


if __name__ == "__main__":
    print("Hi Caravan!")
    deck = Deck()
    deck.shuffle()
    print(deck)
    for card in deck.cards[:0]:
        print(card)

    p1 = Player()
    p2 = Player()
    p1.give_hand()
    for card in p1.hand:
        print(card)


