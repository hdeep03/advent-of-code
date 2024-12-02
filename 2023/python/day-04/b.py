import sys

def main():
    #data = sys.stdin.read()
    cards = [0] + [1] * 204
    i = 0
    for line in sys.stdin:
        i+=1
        line = line.split(":")[1]
        first_set, second_set = line.split("|")
        s2 = set()
        for x in second_set.split(" "):
            try:
                x = int(x)
                s2.add(x)
            except:
                continue
        new_cards = 0
        for x in first_set.split():
            try:
                x = int(x)
            except:
                continue
            if x in s2:
                new_cards += 1
        print(new_cards)
        for index in range(i+1, i+new_cards+1):
            cards[index] += cards[i]
        print(cards)
    print(sum(cards))

main()