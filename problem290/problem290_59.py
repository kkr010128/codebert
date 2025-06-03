import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    f = list(map(int,input().split()))
    a.sort()
    f.sort(reverse=True)

    if sum(a) <= K:
        print(0)
    else:
        a = np.array(a)
        f = np.array(f)
        left,right = 0,max(a)*max(f)
        while right-left > 1:
            mid = (left+right)//2
            pra = a-mid//f
            pra[pra<0] = 0
            if np.sum(pra) > K:
                left = mid
            else:
                right = mid
        print(right)

if __name__ == "__main__":
    main()
