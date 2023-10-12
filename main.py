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

POSITION = (
    "hand",
    "deck",
    "car1",
    "car2",
    "car3"
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
        card_to_move = int(input("Choose a card to move: "))-1
        # Check the validity of the card
        if 8 >= card_to_move >= 0:
            cards_in_hand[card_to_move].holder = caravan_no
        else:
            raise Exception("Please enter a valid number!")

    def move_card_to_hand(self):
        """
        Moves the first card in the deck to the hand
        """

        cards_in_deck = self.get_cards("deck")
        if len(self.get_cards("hand")) != 8:
            cards_in_deck[0].holder = "hand"
        else:
            raise Exception("Cannot give out a card to hand!")

    def discard_card(self):
        cards_in_hand = self.get_cards("hand")
        card_to_discard = int(input("Please choose a card to discard"))-1
        # Check the validity of the card
        if 8 >= card_to_discard >= 0:
            cards_in_hand[card_to_discard].holder = "deck"
        else:
            raise Exception("Please enter a valid number!")

    def discard_caravan(self):
        caravan_no = int(input("Enter a caravan to discard"))
        cards_in_hand = self.get_cards(caravan_no)
        caravan_to_discard = caravan_no
        # Check the validity of the card
        if 3 >= caravan_to_discard >= 0:
            cards_in_hand[caravan_to_discard].holder = "deck"
        else:
            raise Exception("Please enter a valid number!")



if __name__ == "__main__":
    print("Hi Caravan!")
    '''

    num_cards_in_deck = len(deck.get_cards('deck'))
    print(f"Cards in deck: {num_cards_in_deck}")

    '''

    P1 = Player()
    P2 = Player()

    P1.deck = Deck()
    P1.deck.shuffle()

    P1.deck.deal()
    for card in P1.deck.get_cards("hand"):
        print(card)

    P1.deck.move_card_to_caravan("car1")

    for card in P1.deck.get_cards("car1"):
        print(card)
