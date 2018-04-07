from enum import Enum


class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Deck:

    def __init__(self, cards):
        """
        :argument cards all cards dealt or not as a list
        :argument dealIndex
        """
        self.cards = cards
        self.dealIndex = 0

    def shuttle(self):
        pass

    def nb_remaining_cards(self):
        return len(self.cards) - self.dealIndex

    def deal_card(self):
        pass


class Card:

    def __init__(self, face_value:int, suit: Suit):
        self.face_value = face_value
        self.suit = suit
        self.__available = True

    def card_available(self):
        return self.__available

    def mark_unavailable(self):
        self.__available = False

    def value(self):
        return self.face_value


class Hand:

    def __init__(self):
        self.__cards = []

    def add_card(self, card):
        self.__cards.append(card)

    def score(self):
        score = 0
        for card in self.__cards:
            score += card.face_value
        return score


