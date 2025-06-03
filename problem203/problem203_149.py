from math import ceil, floor

def main():
    a, b = map(int, input().split())
    p8_l = ceil(a / 0.08)
    p8_h = int((a+1) // 0.08)
    p10_l = int(b / 0.10)
    p10_h = int((b+1) / 0.10) - 1
    if p8_h >= p10_h >= p8_l and p8_l >= p10_l:
        print(p8_l)
    elif p8_l <= p10_l <= p8_h and p8_l <= p10_l:
        print(p10_l)
    else:
        print(-1)
    
if __name__ == '__main__':
    main()