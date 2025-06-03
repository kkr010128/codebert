import sys
input = sys.stdin.readline

def main():
    n = int(input())

    stick = list(map(int, input().split()))

    total = sum(stick)
    mid = total // 2

    cum = 0
    midi = 0
    for i, block in enumerate(stick):
        cum += block
        if cum >= mid:
            midi = i
            break

    l1 = cum
    r1 = total - l1
    diff1 = abs(l1 - r1)
    
    l2 = l1 - stick[midi]
    r2 = r1 + stick[midi]
    diff2 = abs(l2 - r2)
    
    print(min(diff1, diff2))

main()