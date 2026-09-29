import random

import pytest

from engine.cards import Card, Deck, Rank, Suit


def test_card_converts_to_and_from_text() -> None:
    card = Card.from_text("As")

    assert card == Card(Rank.ACE, Suit.SPADES)
    assert str(card) == "As"


def test_ten_is_written_as_t() -> None:
    assert str(Card(Rank.TEN, Suit.HEARTS)) == "Th"


@pytest.mark.parametrize("text", ["", "A", "Asd", "1s", "Ax"])
def test_invalid_card_text_raises(text: str) -> None:
    with pytest.raises(ValueError):
        Card.from_text(text)


def test_ranks_compare_by_strength() -> None:
    assert Rank.ACE > Rank.KING > Rank.TWO


def test_new_deck_has_52_unique_cards() -> None:
    deck = Deck()

    cards = deck.deal(52)

    assert len(set(cards)) == 52
    assert deck.remaining == 0


def test_dealing_removes_cards_from_the_deck() -> None:
    deck = Deck()

    hand = deck.deal(2)

    assert len(hand) == 2
    assert deck.remaining == 50


def test_same_seed_gives_same_shuffle() -> None:
    first = Deck(random.Random(42)).deal(52)
    second = Deck(random.Random(42)).deal(52)

    assert first == second


def test_different_seeds_give_different_shuffles() -> None:
    first = Deck(random.Random(1)).deal(52)
    second = Deck(random.Random(2)).deal(52)

    assert first != second


def test_dealing_more_cards_than_remain_raises() -> None:
    deck = Deck()
    deck.deal(50)

    with pytest.raises(ValueError):
        deck.deal(3)
