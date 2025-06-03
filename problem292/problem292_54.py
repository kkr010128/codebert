import sys


# input = sys.stdin.readline

def main():
    N = int(input())
    d = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i !=j:
                ans += d[i]*d[j]



    print(int(ans/2))

if __name__ == "__main__":
    main()