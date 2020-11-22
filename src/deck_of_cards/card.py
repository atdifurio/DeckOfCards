"""@package deck_of_cards.card

@brief Card class
"""


class Card:
    """Card class with rank, suit, rank_name, suit_name, and suit_color"""

    SUITS = ["hearts", "diamonds", "spades", "clubs"]
    RANKS = [
        None,
        "Ace",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]
    COLOR_TO_SUIT_MAPPING = {
        "hearts": "red",
        "diamonds": "red",
        "spades": "black",
        "clubs": "black",
    }

    def __init__(self, rank: int, suit: int):
        self._rank = rank
        self._suit = suit

    @property
    def suit(self) -> int:
        return self._suit

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def rank_name(self) -> str:
        return self.RANKS[self.rank]

    @property
    def suit_name(self) -> str:
        return self.SUITS[self.suit]

    @property
    def suit_color(self) -> str:
        return self.COLOR_TO_SUIT_MAPPING[self.SUITS[self.suit]]

    def __str__(self):
        return "%s of %s" % (self.RANKS[self.rank], self.suit_name)

    def __repr__(self):
        return "<Card with suit: %d, rank: %d>" % (self.suit, self.rank)
