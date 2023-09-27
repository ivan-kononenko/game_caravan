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
        num_in_deck = len(self.get_cards("deck"))
        num_in_hand = len(self.get_cards("hand"))
        num_in_caravans = (
                len(self.get_cards("caravan_1"))
                + len(self.get_cards("caravan_2"))
                + len(self.get_cards("caravan_3"))
        )
        return f"Deck of {len(self.cards)} ({num_in_deck}, {num_in_hand}, {num_in_caravans}) cards."

    def shuffle(self):
        """
        Randomize deck
        """
        return random.shuffle(self.cards)

    def get_cards(self, location):
        """
        Return cards reside in a particular location provided in the parameter
        """
        result_cards = []
        for card in self.cards:
            if card.holder == location:
                result_cards.append(card)
        return result_cards

    def deal(self):
        """
        Initial deal. Assign 8 cards to a player (move to the hand)
        """
        for card in self.cards[:8]:
            card.holder = "hand"

    def move_card_to_caravan(self, caravan_no):
        """
        Moves a card from the hand to a caravan, given in the parameter
        """
        cards_in_hand = self.get_cards("hand")
        # Currently it is a random card
        card_to_move = random.randint(0, len(cards_in_hand))
        cards_in_hand[card_to_move - 1].holder = caravan_no

    def move_card_to_hand(self):
        """
        Moves the first card in the deck to the hand
        """
        cards_in_deck = self.get_cards("deck")
        cards_in_deck[0].holder = "hand"


if __name__ == "__main__":
    print("Hi Caravan!")
    deck = Deck()
    deck.shuffle()
    print(deck)
    deck.deal()

    for card in deck.cards[:]:
        print(card)
    num_cards_in_hand = len(deck.get_cards('hand'))
    print(f"Cards in hand: {num_cards_in_hand}")

    num_cards_in_deck = len(deck.get_cards('deck'))
    print(f"Cards in hand: {num_cards_in_deck}")

    deck.shuffle()
    deck.move_card_to_caravan("caravan_1")
    deck.shuffle()
    deck.move_card_to_caravan("caravan_1")

    for card in deck.cards[:]:
        print(card)

    print(deck)

    # p1 = Player()
    # p2 = Player()
    # p1.give_hand()
    # for card in p1.hand:
    #     print(card)


