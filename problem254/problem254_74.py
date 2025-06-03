import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    a = int(input())
    b = int(input())
    if a + b == 3:
        print(3)
        return
    elif a + b == 4:
        print(2)
        return
    print(1)
    
    
main()