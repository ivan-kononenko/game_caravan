# game_caravan




# TODO
√ - analyze the code, prepare questions
√ - write __str__ for Deck class
√ - write method "deal" of class Deck
- find error in function move_card_to_caravan
- change funtion move_card_to_caravan:
  add checking if location already occupied by a card.
  If so, return error (raise exception)


# Notes
- Create Player class
  - in init create Deck and assign to Deck class (same as cards and deck)

Треба зробити константу (як ranks/Suits) card_position, котра має 5 значення: deck, card, car1, car2, car3.

Caravan_no замінити на location. Меетод в move_card

1. Здати карти
2. Перемішати карти
3. Пут кард для 3 карти, змінюється 3 з усіх, чи 3 з руки??