import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    s, t = input().split()
    print(t, end="")
    print(s)
    
    
    
main()
