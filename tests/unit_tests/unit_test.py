import os
import pytest

from deck_of_cards.deck import Deck
from deck_of_cards.card import Card


@pytest.fixture
def deck_of_cards():
    return Deck()


@pytest.fixture
def card():
    return Card(1, 1)


def test_log_level_with_none_set():
    os.environ["DECK_LOG_LEVEL"] = ""
    # import has to be done here so I can set env var first
    from deck_of_cards.logger import logger

    assert logger.level == 20


def test_deck_str(deck_of_cards):
    cmp_str = "Deck with 52 cards"
    assert str(deck_of_cards) == cmp_str


def test_deck_shuffling(deck_of_cards):
    orig_deck = list(deck_of_cards._deck)
    # If I shuffle 100 times at least 1 time should be different
    checker = False
    for i in range(100):
        deck_of_cards.shuffle()
        if orig_deck != deck_of_cards._deck:
            checker = True
    assert checker


def test_shuffling_a_deck_with_two_cards(deck_of_cards):
    for i in range(len(deck_of_cards) - 2):
        deck_of_cards.deal_card()
    assert len(deck_of_cards) == 2
    orig_deck = list(deck_of_cards._deck)
    # If I shuffle 100 times at least 1 time should be different
    checker = False
    for i in range(100):
        deck_of_cards.shuffle()
        if orig_deck != deck_of_cards._deck:
            checker = True
    assert checker


def test_shuffling_a_deck_with_one_cards(deck_of_cards):
    for i in range(len(deck_of_cards) - 1):
        deck_of_cards.deal_card()
    assert len(deck_of_cards) == 1
    orig_deck = list(deck_of_cards._deck)
    # If I shuffle 100 times at least no times should be different
    checker = True
    for i in range(100):
        deck_of_cards.shuffle()
        if orig_deck != deck_of_cards._deck:
            checker = False
    assert checker


def test_shuffling_a_deck_with_no_cards(deck_of_cards):
    for i in range(len(deck_of_cards)):
        deck_of_cards.deal_card()
    assert len(deck_of_cards) == 0
    orig_deck = list(deck_of_cards._deck)
    deck_of_cards.shuffle()
    assert orig_deck == deck_of_cards._deck


def test_deck_repr(deck_of_cards):
    cmp_str = "<Deck of 52 cards and self._deck = [<Card with suit: 0, rank: 1>, <Card with suit: 1, rank: 1>, <Card with suit: 2, rank: 1>, <Card with suit: 3, rank: 1>, <Card with suit: 0, rank: 2>, <Card with suit: 1, rank: 2>, <Card with suit: 2, rank: 2>, <Card with suit: 3, rank: 2>, <Card with suit: 0, rank: 3>, <Card with suit: 1, rank: 3>, <Card with suit: 2, rank: 3>, <Card with suit: 3, rank: 3>, <Card with suit: 0, rank: 4>, <Card with suit: 1, rank: 4>, <Card with suit: 2, rank: 4>, <Card with suit: 3, rank: 4>, <Card with suit: 0, rank: 5>, <Card with suit: 1, rank: 5>, <Card with suit: 2, rank: 5>, <Card with suit: 3, rank: 5>, <Card with suit: 0, rank: 6>, <Card with suit: 1, rank: 6>, <Card with suit: 2, rank: 6>, <Card with suit: 3, rank: 6>, <Card with suit: 0, rank: 7>, <Card with suit: 1, rank: 7>, <Card with suit: 2, rank: 7>, <Card with suit: 3, rank: 7>, <Card with suit: 0, rank: 8>, <Card with suit: 1, rank: 8>, <Card with suit: 2, rank: 8>, <Card with suit: 3, rank: 8>, <Card with suit: 0, rank: 9>, <Card with suit: 1, rank: 9>, <Card with suit: 2, rank: 9>, <Card with suit: 3, rank: 9>, <Card with suit: 0, rank: 10>, <Card with suit: 1, rank: 10>, <Card with suit: 2, rank: 10>, <Card with suit: 3, rank: 10>, <Card with suit: 0, rank: 11>, <Card with suit: 1, rank: 11>, <Card with suit: 2, rank: 11>, <Card with suit: 3, rank: 11>, <Card with suit: 0, rank: 12>, <Card with suit: 1, rank: 12>, <Card with suit: 2, rank: 12>, <Card with suit: 3, rank: 12>, <Card with suit: 0, rank: 13>, <Card with suit: 1, rank: 13>, <Card with suit: 2, rank: 13>, <Card with suit: 3, rank: 13>]>"
    assert repr(deck_of_cards) == cmp_str


def test_deck_reverse(deck_of_cards):
    assert [c for c in reversed(deck_of_cards)] == deck_of_cards._deck


def test_deck_indexing(deck_of_cards):
    assert deck_of_cards[0] is deck_of_cards._deck[0]


def test_card_str(card):
    assert str(card) == "Ace of diamonds"


def test_card_repr(card):
    assert repr(card) == "<Card with suit: 1, rank: 1>"


def test_card_getters(card):
    assert card.rank_name == "Ace"
    assert card.suit_name == "diamonds"
    assert card.suit_color == "red"


def test_init_deck_from_arr():
    deck_list = [
        Card(rank=rank, suit=suit) for rank in range(1, 14) for suit in range(0, 4)
    ]
    deck = Deck(deck=deck_list)
    test_deck_str(deck)
    test_deck_repr(deck)
    test_deck_reverse(deck)
    test_deck_indexing(deck)
