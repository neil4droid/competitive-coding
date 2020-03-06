import math
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Reverse the order of operations and add elements from reverse sorted deck to the array.
        Given order of operations to get a sorted array = pop, shift to bottom.
        Reverse sort the deck.
        Reverse the order of operations: push the highest number, shift it to top.

        Runtime: 44 ms, faster than 72.49% of Python3 online submissions for Reveal Cards In Increasing Order.
        
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reveal Cards In Increasing Order.
        """
        if not deck: return []
        
        deck = sorted(deck, reverse=True)
        arr = []
        for i in range(0, len(deck)):
            arr.insert(0, deck[i])
            if i == len(deck)-1: break
            arr.insert(0, arr[-1])
            del arr[-1]

        return arr