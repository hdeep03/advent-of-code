import sys
import math
from functools import cmp_to_key

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    hands_data = []
    hand_to_value = {}
    for x in data:
        hands_data.append(x.split(" ")[0])
        hand_to_value[x.split(" ")[0]] = int(x.split(" ")[1])
    
    tot = 0
    for i, x in enumerate(sorted(hands_data, key=cmp_to_key(compare))):
        tot += hand_to_value[x] * (i + 1)
    print(tot)



def compare_same_class(hand1: str, hand2: str) -> int:
    lookup = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    for h1, h2 in zip(list(hand1), list(hand2)):
        if lookup.index(h1) < lookup.index(h2):
            return 1
        elif lookup.index(h1) > lookup.index(h2):
            return -1
    return 0

def compare(hand1: str, hand2: str) -> int:
    class1 = classify_hand(hand1)
    class2 = classify_hand(hand2)

    if class1 < class2:
        return -1
    elif class1 > class2:
        return 1
    else:
        return compare_same_class(hand1, hand2)

def classify_hand(hand: str) -> int:
    # 0: high card
    # 1: one pair
    # 2: two pairs
    # 3: three of a kind
    # 4: full house
    # 5: four of a kind
    # 6: 5 of a kind
    counts = {}
    for x in hand:
        counts[x] = counts.get(x, 0) + 1

    if len(counts) == 5:
        return 0
    elif len(counts) == 4:
        return 1
    elif len(counts) == 3 and max(counts.values()) == 2:
        return 2
    elif len(counts) == 3:
        return 3
    elif len(counts) == 2 and max(counts.values()) == 3:
        return 4
    elif len(counts) == 2:
        return 5
    elif len(counts) == 1:
        return 6
    else:
        raise Exception(f"Invalid hand: {hand}")


main()