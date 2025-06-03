import numpy as np
from numba import njit

@njit
def get_div_nums(n):
    divs = np.ones(n+1, dtype=np.int64)
    for i in range(2, n):
        divs[i::i] += 1
    return divs

def main():
    N = int(input())
    divs = get_div_nums(N)
    ans = divs[:N].sum()-1
    print(ans)
    #print(divs[:20])

if __name__ == "__main__":
    main()