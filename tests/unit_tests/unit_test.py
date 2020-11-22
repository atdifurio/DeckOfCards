import os
import pytest

from deck_of_cards.deck import Deck
from deck_of_cards.card import Card

@pytest.fixture
def deck_of_cards():
    return Deck()

@pytest.fixture
def card():
    return Card(1,1)

def test_log_level_with_none_set():
    os.environ["DECK_LOG_LEVEL"] = ""
    # import has to be done here so I can set env var first
    from deck_of_cards.logger import logger
    assert logger.level == 20

def test_deck_str(deck_of_cards):
    cmp_str = 'Deck with 52 cards'
    assert str(deck_of_cards) == cmp_str


def test_deck_repr(deck_of_cards):
    cmp_str = '<Deck of 52 cards and self._deck = [<Card with suit: 0, rank: 1>, <Card with suit: 1, rank: 1>, <Card with suit: 2, rank: 1>, <Card with suit: 3, rank: 1>, <Card with suit: 0, rank: 2>, <Card with suit: 1, rank: 2>, <Card with suit: 2, rank: 2>, <Card with suit: 3, rank: 2>, <Card with suit: 0, rank: 3>, <Card with suit: 1, rank: 3>, <Card with suit: 2, rank: 3>, <Card with suit: 3, rank: 3>, <Card with suit: 0, rank: 4>, <Card with suit: 1, rank: 4>, <Card with suit: 2, rank: 4>, <Card with suit: 3, rank: 4>, <Card with suit: 0, rank: 5>, <Card with suit: 1, rank: 5>, <Card with suit: 2, rank: 5>, <Card with suit: 3, rank: 5>, <Card with suit: 0, rank: 6>, <Card with suit: 1, rank: 6>, <Card with suit: 2, rank: 6>, <Card with suit: 3, rank: 6>, <Card with suit: 0, rank: 7>, <Card with suit: 1, rank: 7>, <Card with suit: 2, rank: 7>, <Card with suit: 3, rank: 7>, <Card with suit: 0, rank: 8>, <Card with suit: 1, rank: 8>, <Card with suit: 2, rank: 8>, <Card with suit: 3, rank: 8>, <Card with suit: 0, rank: 9>, <Card with suit: 1, rank: 9>, <Card with suit: 2, rank: 9>, <Card with suit: 3, rank: 9>, <Card with suit: 0, rank: 10>, <Card with suit: 1, rank: 10>, <Card with suit: 2, rank: 10>, <Card with suit: 3, rank: 10>, <Card with suit: 0, rank: 11>, <Card with suit: 1, rank: 11>, <Card with suit: 2, rank: 11>, <Card with suit: 3, rank: 11>, <Card with suit: 0, rank: 12>, <Card with suit: 1, rank: 12>, <Card with suit: 2, rank: 12>, <Card with suit: 3, rank: 12>, <Card with suit: 0, rank: 13>, <Card with suit: 1, rank: 13>, <Card with suit: 2, rank: 13>, <Card with suit: 3, rank: 13>]>'
    assert repr(deck_of_cards) == cmp_str

def test_deck_reverse(deck_of_cards):
    assert [c for c in reversed(deck_of_cards)] == deck_of_cards._deck

def test_deck_indexing(deck_of_cards):
    assert deck_of_cards[0] is deck_of_cards._deck[0]

def test_card_str(card):
    assert str(card) == 'Ace of diamonds'

def test_card_repr(card):
    assert repr(card) == '<Card with suit: 1, rank: 1>'

def test_card_getters(card):
    assert card.rank_name == 'Ace'
    assert card.suit_name == 'diamonds'
    assert card.suit_color == 'red'

def test_init_deck_from_arr():
    deck_list = [Card(rank=rank, suit=suit) for rank in range(1, 14) for suit in range(0, 4)]
    d = Deck(deck=deck_list)
    test_deck_str(d)
    test_deck_repr(d)
    test_deck_reverse(d)
    test_deck_indexing(d)





