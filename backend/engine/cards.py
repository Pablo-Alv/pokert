"""Playing cards and a shuffled 52-card deck."""

import random
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Self


class Rank(IntEnum):
    """A card's rank. The number is its strength, so ranks compare: ACE > KING."""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    """A card's suit. The value is its one-letter code."""

    CLUBS = "c"
    DIAMONDS = "d"
    HEARTS = "h"
    SPADES = "s"


# One-character codes for each rank, e.g. Rank.TEN <-> "T".
RANK_SYMBOLS: dict[Rank, str] = dict(zip(Rank, "23456789TJQKA", strict=True))
SYMBOL_RANKS: dict[str, Rank] = {symbol: rank for rank, symbol in RANK_SYMBOLS.items()}


@dataclass(frozen=True)
class Card:
    """One playing card. Frozen means it can't be changed after it's created."""

    rank: Rank
    suit: Suit

    def __str__(self) -> str:
        return f"{RANK_SYMBOLS[self.rank]}{self.suit.value}"

    @classmethod
    def from_text(cls, text: str) -> Self:
        """Build a card from a two-letter code like "As" (ace of spades)."""
        if len(text) != 2 or text[0] not in SYMBOL_RANKS:
            raise ValueError(f"Not a card: {text!r}")
        try:
            suit = Suit(text[1])
        except ValueError:
            raise ValueError(f"Not a card: {text!r}") from None
        return cls(SYMBOL_RANKS[text[0]], suit)


class Deck:
    """A shuffled 52-card deck that cards are dealt from the top of."""

    def __init__(self, rng: random.Random | None = None) -> None:
        # Pass a seeded rng, e.g. random.Random(42), to get a repeatable shuffle.
        self._cards = [Card(rank, suit) for suit in Suit for rank in Rank]
        (rng or random.Random()).shuffle(self._cards)

    @property
    def remaining(self) -> int:
        return len(self._cards)

    def deal(self, count: int) -> list[Card]:
        """Remove and return `count` cards from the top of the deck."""
        if count > len(self._cards):
            raise ValueError(f"Can't deal {count} cards, only {len(self._cards)} left")
        dealt = self._cards[:count]
        del self._cards[:count]
        return dealt
