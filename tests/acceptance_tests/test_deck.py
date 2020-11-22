from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import cfparse

import pytest

from deck_of_cards.deck import Deck

LEGAL_DECK_PARAMETERS = {
    "length": 52,
    "num_ranks": 13,
    "num_suits": 4,
    "face_cards": 12,
    "face_card_ranks": [11, 12, 13],
}


@scenario("../features/deck.feature", "Try to create a legal deck of cards")
def test_create_legal_size_deck_of_cards():
    pass


@scenario("../features/deck.feature", "Try to create a legal shuffled deck of cards")
def test_create_legal_shuffled_size_deck_of_cards():
    pass


@scenario("../features/deck.feature", "Deal 1 card")
def test_deal_one_card():
    pass


@scenario("../features/deck.feature", "Deal 3 cards")
def test_deal_three_cards():
    pass


@scenario("../features/deck.feature", "Deal 52 cards")
def test_deal_52_cards():
    pass


@scenario("../features/deck.feature", "Deal 53 cards")
def test_deal_53_cards():
    pass


@scenario("../features/deck.feature", "Deal 0 cards")
def test_deal_zero_cards():
    pass


@scenario("../features/deck.feature", "Deal 3 cards from a shuffled deck")
def test_deal_three_cards_from_a_shuffled_deck():
    pass


@scenario("../features/deck.feature", "Try to create a legal shuffled deck of cards")
def test_create_legal_shuffled_deck():
    pass


@scenario("../features/deck.feature", "Deal 53 cards and check the 53rd is None")
def test_dealing_from_empty_deck_returns_none():
    pass


@pytest.fixture
@given("a deck of cards")
def deck_of_cards():
    return Deck()


@given("I shuffle the deck")
def shuffle_the_deck(deck_of_cards):
    deck_of_cards.shuffle()


@pytest.fixture
@when(cfparse("I deal {count:Number} cards", extra_types=dict(Number=int)))
def deal_cards(count, deck_of_cards):
    delt = [deck_of_cards.deal_card() for i in range(count)]
    return delt


@then("I should have a deck")
def got_deck():
    pass


@then(
    cfparse("the deck should have {count:Number} cards", extra_types=dict(Number=int))
)
def check_card_count(count, deck_of_cards):
    assert len(deck_of_cards) == count


@then(
    cfparse("the deck should have {count:Number} ranks", extra_types=dict(Number=int))
)
def check_ranks_count(count, deck_of_cards):
    assert len(set(c.rank for c in deck_of_cards)) == count


@then(
    cfparse("the deck should have {count:Number} suits", extra_types=dict(Number=int))
)
def check_suits(count, deck_of_cards):
    assert len(set(c.suit for c in deck_of_cards)) == count


@then(
    cfparse(
        "the deck should have {count:Number} face cards", extra_types=dict(Number=int)
    )
)
def check_face_cards(count, deck_of_cards):
    assert (
        sum(
            1
            for c in deck_of_cards
            if c.rank in LEGAL_DECK_PARAMETERS["face_card_ranks"]
        )
        == count
    )


@then(
    cfparse("the deck should have {count:Number} cards", extra_types=dict(Number=int))
)
def check_deck_after_dealing(count, deck_of_cards):
    assert len(deck_of_cards) == count


@then(
    cfparse(
        "the receiver should have {count:Number} cards", extra_types=dict(Number=int)
    )
)
def check_delt_cards(count, deal_cards):
    assert len(deal_cards) == count


@then(cfparse("the next card I deal should be None"))
def check_next_card_is_none(deck_of_cards):
    next_card = deck_of_cards.deal_card()
    assert next_card is None
