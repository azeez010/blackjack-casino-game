from blackjackcore import BlackJackCore
from card import Card


class BlackJack:
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # The suit value
    suits_values = {"Spades": "\u2664", "Hearts": "\u2661",
                    "Clubs": "\u2667", "Diamonds": "\u2662"}

    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # The card value
    cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

    # The deck of cards
    deck = []

    def __init__(self):
        self.load_cards()

    def load_cards(self):
        # Loop for every type of suit
        for suit in self.suits:

            # Loop for every type of card in a suit
            for card in self.cards:

                # Adding card to the deck
                self.deck.append(Card(self.suits_values[suit], card, self.cards_values[card]))

    def start_blackjack_game(self):
        core = BlackJackCore()
        core.blackjack_game(self.deck)