import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(-1)
        return
    print(a*b)
    
    
main()
