# 💫 Blackjack Card Game
This is a command-line implementation of the classic Blackjack card game in Python.

# 🚀 Instruction
1. This is a command-line implementation of the classic Blackjack card game in Python.

2. Run the Python script main.py to start the game.
    # shell
    python main.py

3. Follow the on-screen prompts and make your choices during the game:
    - Enter 'H' to Hit (draw another card).
    - Enter 'S' to Stand (end your turn).

4. Enjoy playing Blackjack!


## Rules
1. The goal is to have a hand value closer to 21 than the dealer's hand value, without going over 21.
2. Numbered cards are worth their face value, face cards (King, Queen, Jack) are worth 10, and the Ace  can be worth either 1 or 11.
3. At the start of the game, you and the dealer are each dealt two cards. One of the dealer's cards is hidden.
4. You can choose to 'Hit' to draw another card, or 'Stand' to end your turn.
5. If your hand value exceeds 21, you 'Bust' and lose the game.
6. After you stand, the dealer reveals their hidden card and draws more cards until their hand value is at least 17.
7. If the dealer's hand value exceeds 21, they 'Bust' and you win the game.
8. If neither you nor the dealer busts, the one with the higher hand value wins.
9. If both hands have the same value, it's a tie game.


# Code Structure
1. `main.py`: The start Python script.
2. `blackjackcore.py`: The class BlackJackCore contains the game logic.
2. `blackjack.py`: The class BlackJack serve as in entry class to the game.
3. `card.py`: The Card class definition, representing a playing card in the game.
4. `utils.py`: The utility function that prints a list of playing cards in a visually appealing format. It is commonly used in card games or applications that involve displaying a player's hand of cards.
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │A        │  │K        │  │Q        │
    │         │  │         │  │         │
    │   ♠️     │  │   ♥️     │  │    ♦️    │
    │         │  │         │  │         │
    │        A│  │        K│  │        Q│
    └─────────┘  └─────────┘  └─────────┘
5. `TerminalClear.py`: The function that clear terminal.

### ⚡ Dependencies
There are no external dependencies required to run this game. It is built using only the Python standard library.

## 💲 License
This project is licensed under the MIT License.

Feel free to modify and enhance the code to suit your requirements.

Enjoy playing Blackjack!
