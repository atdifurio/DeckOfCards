Feature: Deck of Cards
  I can suffle and deal a deck of cards

Scenario: Try to create a legal deck of cards
  Given a deck of cards
  Then I should have a deck
  And the deck should have 52 cards
  And the deck should have 13 ranks
  And the deck should have 4 suits
  And the deck should have 12 face cards

Scenario: Deal 1 card
  Given a deck of cards
  When I deal 1 cards
  Then the deck should have 51 cards
  And the receiver should have 1 cards

Scenario: Deal 3 cards
  Given a deck of cards
  When I deal 3 cards
  Then the deck should have 49 cards

Scenario: Deal 52 cards
  Given a deck of cards
  When I deal 52 cards
  Then the deck should have 0 cards

Scenario: Deal 53 cards
  Given a deck of cards
  When I deal 53 cards
  Then the deck should have 0 cards

Scenario: Deal 53 cards and check the 53rd is None
  Given a deck of cards
  When I deal 52 cards
  Then the next card I deal should be None

Scenario: Deal 0 cards
  Given a deck of cards
  When I deal 0 cards
  Then the deck should have 52 cards

Scenario: Try to create a legal shuffled deck of cards
  Given a deck of cards
  And I shuffle the deck
  Then I should have a deck
  And the deck should have 52 cards
  And the deck should have 13 ranks
  And the deck should have 4 suits
  And the deck should have 12 face cards

Scenario: Deal 3 cards from a shuffled deck
  Given a deck of cards
  And I shuffle the deck
  When I deal 3 cards
  Then the deck should have 49 cards

Scenario: Deal 52 cards and shuffle the deck
  Given a deck of cards
  When I deal 52 cards
  And I shuffle the deck
  Then the deck should have 0 cards
