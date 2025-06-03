from itertools import starmap
print("".join(starmap(lambda c: c.lower() if 'A' <= c <= 'Z' else c.upper(), input())))