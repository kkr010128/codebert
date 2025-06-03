"""A."""

import sys

input = sys.stdin.readline  # noqa: A001

D, T, S = map(int, input()[:-1].split(' '))

print('Yes' if T * S >= D else 'No')
