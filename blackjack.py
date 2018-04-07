from deck import Hand, Card


class BlackJackHand(Hand):

    def __init__(self):
        super(BlackJackHand, self).__init__()

    def possible_score(self):
        """
        FIXME
        :return:
        """
        return []

    def score(self):
        max_under = -1
        min_over = 1000
        for score in self.possible_score():
            if 21 < score < min_over:
                min_over = 100
            elif 21 >= score > max_under:
                max_under = score
        return min_over if max_under == 0 else max_under

    def busted(self):
        return self.score() > 21

    def is_21(self):
        return self.score() == 21

    def is_blackjack(self):
        pass


class BlackJackCard(Card):
    
    def __init__(self, face_value, suit):
        super(BlackJackCard, self).__init__(face_value, suit)

    def min_value(self):
        return 1 if (self.__is_ace()) else self.face_value

    def max_value(self):
        return 11 if (self.__is_ace()) else self.face_value

    def __is_ace(self):
        return self.face_value == 1

    def is_face_card(self):
        return 11 <= self.face_value <= 13
