import numpy as np

def solve():
    for i in range(K,N):
        if A[i-K] < A[i]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    N,K = list(map(int, input().split()))  
    A = list(map(int, input().split()))  
    solve()
