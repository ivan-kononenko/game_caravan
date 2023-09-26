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
        self.hand += self.deck.cards[:8]
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

    def __str__(self):
        return f"Deck currently has {len(self.cards)} cards."

    def shuffle(self):
        """
        Randomize deck
        """
        return random.shuffle(self.cards)

    def get_cards(self, location):
        result_cards = []
        for card in self.cards:
            if card.holder == location:
                result_cards.append(card)
        return result_cards

    def deal(self):
        """
        Initial deal. Assign cards to player
        """
        for card in self.cards[:8]:
            card.holder = "hand"

    def put_card(self, caravan_no):
        what_card = 3
        cards_in_hand = self.get_cards("hand")
        cards_in_hand[what_card].holder = caravan_no


if __name__ == "__main__":
    print("Hi Caravan!")
    deck = Deck()
    deck.shuffle()
    print(deck)
    deck.deal()

    for card in deck.cards[:20]:
        print(card)
    num_cards_in_hand = len(deck.get_cards('hand'))
    print(f"Cards in hand: {num_cards_in_hand}")

    num_cards_in_deck = len(deck.get_cards('deck'))
    print(f"Cards in hand: {num_cards_in_deck}")

    deck.put_card("caravan_1")

    for card in deck.cards[:20]:
        print(card)
    num_cards_in_hand = len(deck.get_cards('hand'))
    print(f"Cards in hand: {num_cards_in_hand}")

    num_cards_in_deck = len(deck.get_cards('deck'))
    print(f"Cards in hand: {num_cards_in_deck}")

    # p1 = Player()
    # p2 = Player()
    # p1.give_hand()
    # for card in p1.hand:
    #     print(card)


