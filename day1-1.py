import utils
import re

lines = utils.load_lines("day1.txt")

def get_digits(line):
    digits = re.sub(r"[^\d]","",line)
    return int(digits[0] + digits[-1])
digits = [get_digits(x) for x in lines]

print(sum(digits))
