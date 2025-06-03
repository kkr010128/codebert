import string
from collections import Counter


def count(s):
    """Count the occurence of each alphabet chars.
    The count is done case insensitively.

    >>> count('A:a b')  # doctest: +NORMALIZE_WHITESPACE
    Counter({'a': 2, 'b': 1})
    """
    return Counter([c for c in s.lower() if c.isalpha()])


def run():
    s = ''
    while True:
        try:
            s += input()
        except EOFError:
            break

    c = count(s)
    for a in string.ascii_lowercase:
        print(a, ':', c[a])


if __name__ == '__main__':
    run()

