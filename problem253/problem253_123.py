import sys
input = sys.stdin.readline
 
 
def main():
    n,a,b = [int(i) for i in input().strip().split()]
    if (b-a) % 2 == 0:
        print(abs(b - a) // 2)
    else:
        ans = min(a - 1, n - b) + 1 + (b - a - 1) // 2
        print(ans)
    return 
 
 
 
if __name__ == "__main__":
    main()