#!/usr/bin/python

import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    _ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    _suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self._suits
                                       for rank in self._ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


