import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

    
    
main()