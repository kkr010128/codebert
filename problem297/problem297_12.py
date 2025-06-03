import sys
import decimal # 10進法に変換，正確な計算

def input():
    return sys.stdin.readline().strip()

def main():
    n = int(input())
    n = decimal.Decimal(n)
    if n % 2 == 0:
        print(1/decimal.Decimal(2))
        return
    
    print(((n-1)/2+1)/n)

    
    
main()