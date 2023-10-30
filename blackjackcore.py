import random
from utils import Utils


class BlackJackCore:
    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []

    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    def __deal_cards(self, deck):
        Utils.terminal_clear()

        while len(self.player_cards) < 2:

            # Randomly dealing a card
            player_card = random.choice(deck)
            self.player_cards.append(player_card)
            deck.remove(player_card)

            # Updating the player score
            self.player_score += player_card.card_value

            # In case both the cards are Ace, make the first ace value as 1
            if len(self.player_cards) == 2:
                if self.player_cards[0].card_value == 11 and self.player_cards[1].card_value == 11:
                    self.player_cards[0].card_value = 1
                    self.player_score -= 10

            # Print player cards and score
            print("PLAYER CARDS: ")
            Utils.print_cards(self.player_cards, False)
            print("PLAYER SCORE = ", self.player_score)

            input()

            # Randomly dealing a card
            dealer_card = random.choice(deck)
            self.dealer_cards.append(dealer_card)
            deck.remove(dealer_card)

            # Updating the dealer score
            self.dealer_score += dealer_card.card_value

            # Print dealer cards and score, keeping in mind to hide the second card and score
            print("DEALER CARDS: ")
            if len(self.dealer_cards) == 1:
                Utils.print_cards(self.dealer_cards, False)
                print("DEALER SCORE = ", self.dealer_score)
            else:
                Utils.print_cards(self.dealer_cards[:-1], True)
                print("DEALER SCORE = ", self.dealer_score -
                    self.dealer_cards[-1].card_value)

            # In case both the cards are Ace, make the second ace value as 1
            if len(self.dealer_cards) == 2:
                if self.dealer_cards[0].card_value == 11 and self.dealer_cards[1].card_value == 11:
                    self.dealer_cards[1].card_value = 1
                    self.dealer_score -= 10

            input()

        # Player gets a blackjack
        if self.player_score == 21:
            print("PLAYER HAS A BLACKJACK!!!!")
            print("PLAYER WINS!!!!")
            quit()

        Utils.terminal_clear()

        # Print dealer and player cards
        print("DEALER CARDS: ")
        Utils.print_cards(self.dealer_cards[:-1], True)
        print("DEALER SCORE = ", self.dealer_score - self.dealer_cards[-1].card_value)

        print()

        print("PLAYER CARDS: ")
        Utils.print_cards(self.player_cards, False)
        print("PLAYER SCORE = ", self.player_score)

    def __manage_moves(self, deck):
        while self.player_score < 21:
            choice = input("Enter H to Hit or S to Stand : ")

            # Sanity checks for player's choice
            if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
                Utils.terminal_clear()
                print("Wrong choice!! Try Again")

            # If player decides to HIT
            if choice.upper() == 'H':

                # Dealing a new card
                player_card = random.choice(deck)
                self.player_cards.append(player_card)
                deck.remove(player_card)

                # Updating player score
                self.player_score += player_card.card_value

                # Updating player score in case player's card have ace in them
                c = 0
                while self.player_score > 21 and c < len(self.player_cards):
                    if self.player_cards[c].card_value == 11:
                        self.player_cards[c].card_value = 1
                        self.player_score -= 10
                        c += 1
                    else:
                        c += 1

                Utils.terminal_clear()

                # Print player and dealer cards
                print("DEALER CARDS: ")
                Utils.print_cards(self.dealer_cards[:-1], True)
                print("DEALER SCORE = ", self.dealer_score -
                    self.dealer_cards[-1].card_value)

                print()

                print("PLAYER CARDS: ")
                Utils.print_cards(self.player_cards, False)
                print("PLAYER SCORE = ", self.player_score)

            # If player decides to Stand
            if choice.upper() == 'S':
                break

        Utils.terminal_clear()

        # Print player and dealer cards
        print("PLAYER CARDS: ")
        Utils.print_cards(self.player_cards, False)
        print("PLAYER SCORE = ", self.player_score)

        print()
        print("DEALER IS REVEALING THE CARDS....")

        print("DEALER CARDS: ")
        Utils.print_cards(self.dealer_cards, False)
        print("DEALER SCORE = ", self.dealer_score)

    def __check_wins_and_calc_scores(self, deck):
        # Check if player has a Blackjack
        if self.player_score == 21:
            print("PLAYER HAS A BLACKJACK")
            quit()

        # Check if player busts
        if self.player_score > 21:
            print("PLAYER BUSTED!!! GAME OVER!!!")
            quit()

        input()

        # Managing the dealer moves
        while self.dealer_score < 17:
            Utils.terminal_clear()

            print("DEALER DECIDES TO HIT.....")

            # Dealing card for dealer
            dealer_card = random.choice(deck)
            self.dealer_cards.append(dealer_card)
            deck.remove(dealer_card)

            # Updating the dealer's score
            self.dealer_score += dealer_card.card_value

            # Updating player score in case player's card have ace in them
            c = 0
            while self.dealer_score > 21 and c < len(self.dealer_cards):
                if self.dealer_cards[c].card_value == 11:
                    self.dealer_cards[c].card_value = 1
                    self.dealer_score -= 10
                    c += 1
                else:
                    c += 1

            # print player and dealer cards
            print("PLAYER CARDS: ")
            Utils.print_cards(self.player_cards, False)
            print("PLAYER SCORE = ", self.player_score)

            print()

            print("DEALER CARDS: ")
            Utils.print_cards(self.dealer_cards, False)
            print("DEALER SCORE = ", self.dealer_score)

            input()

        # Dealer busts
        if self.dealer_score > 21:
            print("DEALER BUSTED!!! YOU WIN!!!")
            quit()

        # Dealer gets a blackjack
        if self.dealer_score == 21:
            print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
            quit()

        # TIE Game
        if self.dealer_score == self.player_score:
            print("TIE GAME!!!!")

        # Player Wins
        elif self.player_score > self.dealer_score:
            print("PLAYER WINS!!!")

        # Dealer Wins
        else:
            print("DEALER WINS!!!")



    # Function for a single game of blackjack
    def blackjack_game(self, deck):
        # Initial dealing for player and dealer
        self.__deal_cards(deck)
        # Managing the player moves
        self.__manage_moves(deck)
        # Check wins and calculate scores
        self.__check_wins_and_calc_scores(deck)
        