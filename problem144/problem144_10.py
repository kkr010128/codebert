import io
import sys
import math

def solve():
    A, B, H, M = list(map(int, input().split()))
    C_sq = A**2 + B**2 - 2*A*B*math.cos((H - 11/60 * M)*math.pi/6)
    C = math.sqrt(C_sq)
    print(C) 


if __name__ == "__main__":
    solve()