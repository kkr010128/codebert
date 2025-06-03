import sys
def input():
    return sys.stdin.readline()[:-1]


def main():
    A, B, C = map(int,input().split())
    K = int(input())
    count = 0
    while A >= B:
        B = B * 2
        count += 1
    while B >= C:
        C = C * 2
        count += 1
    if count <= K:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()