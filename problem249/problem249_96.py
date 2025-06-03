import sys

def main():
    
    input = sys.stdin.readline
    a,b,k = map(int, input().split())
    if a + b <= k:
        print(0,0)
        sys.exit()
    else:    
        if a < k:
            b = b-(k-a)
            a = 0
        else:
            a = a-k
        print(a,b)
            

if __name__ == "__main__":
    main()
