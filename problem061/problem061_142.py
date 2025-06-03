import re

strings = input()


def swapletter(match):
    word = match.group()
    return word.swapcase()


data = re.sub(r"\w+", swapletter, strings)
print(data)
