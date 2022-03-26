import argparse
import random


def password(args):
    temp = args.p
    if len(temp) <= 8:
        while len(temp) < max_length:
            temp += list[random.randint(0, len(list) - 1)]
        return temp
    else:
        return "MORE THAN 8 CHARACTERS ARE ENTERED"


lower = []
upper = []
numbers = []
symbols = []
max_length = 12
for i in range(65, 91):
    upper.append(chr(i))
    lower.append(chr(i + 32))
for i in range(10):
    numbers.append(str(i))
    if chr(i + 33) != "'" and chr(i + 33) != '''"''':
        symbols.append(chr(i + 33))

list = lower + upper + numbers + symbols

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument(
        "p",
        metavar="password",
        type=str,
        default="",
        help="Enter two lowercase characters,uppercase characters,numbers and symbols:",
    )

    args = parser.parse_args()
    print(str(password(args)))
