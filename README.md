# game_caravan




# TODO
- √ - analyze the code, prepare questions
- √ - write __str__ for Deck class
- √ - write method "deal" of class Deck
- √ -  find error in function move_card_to_caravan
- √ -  change funtion move_card_to_caravan:
 add checking if location already occupied by a card.
 If so, return error (raise exception)
- Create player_turn function, which is self-describing(check Notes)
- Implement rudimentary UI
- Create main game cycle


# Notes

Player turn:
- Give out a card
- 1. Move a card to Caravan(done)
  2. Discard a card
  3. Discard a caravan
- If card is moved OR card is discarded, get a new card


Game cycle:
- Show current playing field and hands of players
- Player 1 turn
- Show current playing field and hands of players
- Player 2 turn
- Show current playing field and hands of players
- Repeat cycle from step 2 until end.

End game conditions:
- All caravans are filled correctly(21 to 26)
- Winner has 2 or more winning caravans