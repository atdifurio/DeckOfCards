"""@package deck_of_cards.deck

@brief Deck class for managing a deck of cards
"""

from random import randint
from typing import List, Optional

from deck_of_cards.card import Card
from deck_of_cards.logger import logger


class Deck:
    """ Deck class with shuffle() and deal_card()"""

    def __init__(self, deck: List[Card] = None, logging=logger):
        self.logging = logging
        self.logging.info("Creating a deck of cards")
        if deck:
            self._deck = deck
        else:
            self._deck = self._create_deck()
        self.logging.debug(f"Initialized deck of cards to: {self._deck}")

    def __getitem__(self, index: int) -> Card:
        return self._deck[index]

    def __iter__(self):
        """Order is flipped to allow deal card as you iter
        otherwise you have a modify list as you go problem and only
        deal half the deck per iter
        """
        return reversed(self._deck)

    def __len__(self):
        return len(self._deck)

    def __reversed__(self):
        """Order is flipped to allow deal card with iter
        otherwise you have a modify list as you go problem and only
        deal half the deck per iter
        """
        return self._deck

    def __str__(self):
        return f"Deck with {len(self._deck)} cards"

    def __repr__(self):
        return (
            f"<Deck of {str(len(self._deck))} cards and self._deck = {str(self._deck)}>"
        )

    @classmethod
    def _create_deck(cls) -> List[Card]:
        """Helper function to initialize Cards in a deck
        """
        return [
            Card(rank=rank, suit=suit) for rank in range(1, 14) for suit in range(0, 4)
        ]

    def shuffle(self):
        """Follows Fisher-Yates alg. for shuffling
        To shuffle an array a of n elements (indices 0..n-1):
          for i from n − 1 downto 1 do
            j ← random integer with 0 ≤ j ≤ i
            exchange a[j] and a[i]
        """
        self.logging.info(f"Shuffling deck")
        self.logging.debug(f"Deck before shuffle: {self._deck}")
        for i in reversed(range(1, len(self._deck))):
            rnd = randint(0, i)
            self._deck[i], self._deck[rnd] = self._deck[rnd], self._deck[i]
        self.logging.debug(f"Deck after shuffle: {self._deck}")

    def deal_card(self) -> Optional[Card]:
        """Deals a card from the top of the deck (end of list)
        """
        self.logging.info(f"Dealing card from deck")
        delt = None
        if self._deck:
            # pop from end to keep consistent with iter
            delt = self._deck.pop()
        self.logging.debug(f"Dealt {str(delt)} from deck")
        return delt
