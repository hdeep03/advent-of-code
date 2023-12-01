import sys

def main():
    tot = 0
    for input_line in sys.stdin:
        tot += 10*_get_first_digit(input_line) + _get_first_digit(input_line[::-1])
    print(tot)

def _get_first_digit(text: str):
    for x in text:
        if x.isdigit():
            return int(x)

main()