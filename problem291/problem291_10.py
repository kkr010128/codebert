import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    c = a - b*2
    if c < 0:
        print(0)
        return
    print(c)
            
    
    
main()
