import sys


def main():
    tot = 0
    for input_line in sys.stdin:
        first, last = _get_outer_digits(input_line)
        tot += 10*first + last
    print(tot)


def _get_outer_digits(text: str):
    numerical_digits = _get_numerical_digits(text)
    text_digits = _get_text_digits(text)
    if not numerical_digits and not text_digits:
        raise ValueError("No digits found in text")
    if not numerical_digits:
        return text_digits[0][1], text_digits[-1][1]
    if not text_digits:
        return numerical_digits[0][1], numerical_digits[-1][1]

    first_digit = min(numerical_digits[0], text_digits[0], key=lambda x: x[0])[1]
    last_digit = max(numerical_digits[-1], text_digits[-1], key=lambda x: x[0])[1]

    return first_digit, last_digit


def _get_numerical_digits(text: str):
    return [(i, int(x)) for i, x in enumerate(text) if x.isdigit()]


def _get_text_digits(text: str):
    text_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    ret = []
    for string, num in text_to_num.items():
        start = text.find(string, 0)
        while start != -1:
            ret.append((start, num))
            start = text.find(string, start+len(string))
    return sorted(ret, key=lambda x: x[0])


main()
