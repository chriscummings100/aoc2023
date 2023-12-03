import utils
import re


lines = utils.load_lines("day1.txt")
print(lines)

NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def find_numbers(line: str) -> str:
    first_index = len(line)
    first_number = -1
    for i in range(1,len(NUMBERS)):
        idx = line.find(NUMBERS[i])
        if idx != -1 and idx < first_index:
            first_number = i
            first_index = idx
        idx = line.find(str(i))
        if idx != -1 and idx < first_index:
            first_number = i
            first_index = idx
    return str(first_number)

def find_numbers_reversed(line:str) -> str:
    last_index = -1
    last_number = -1
    for i in range(1,len(NUMBERS)):
        idx = line.rfind(NUMBERS[i])
        if idx != -1 and idx > last_index:
            last_number = i
            last_index = idx
        idx = line.rfind(str(i))
        if idx != -1 and idx > last_index:
            last_number = i
            last_index = idx
    return str(last_number)

def get_digits(line: str) -> int:

    digits = find_numbers(line) + find_numbers_reversed(line)
    num = int(digits)
    print(f"{line}->{digits}->{num}")
    return num

digits = [get_digits(x) for x in lines]

#sum all values in digits
print(sum(digits))