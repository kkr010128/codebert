def toggle(s):
    """Return a copy of the string with uppercase characters
    converted to lowercase and vice versa.

    >>> toggle("fAIR, LATER, OCCASIONALLY CLOUDY.")
    'Fair, later, occasionally cloudy.'
    """
    return s.swapcase()


def run():
    print(toggle(input()))


run()
