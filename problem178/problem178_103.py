import math  # noqa: F401
from typing import Dict, List, Optional, Tuple, Union  # noqa: F401


def main(A: List[int]):
    print(A[2], A[0], A[1])


if __name__ == "__main__":
    A = list(map(int, input().split()))
    main(A)
