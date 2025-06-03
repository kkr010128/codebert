import sys
input = sys.stdin.buffer.readline

def main():
    T1,T2 = map(int,input().split())
    A1,A2 = map(int,input().split())
    B1,B2 = map(int,input().split())
    l = (A1-B1)*T1 + (A2-B2)*T2
    if l == 0:
        print("infinity")
    elif l > 0:
        if A1 > B1:
            print(0)
        else:
            d = (B1-A1)*T1
            if d%l == 0:
                ans = 2*(d//l)
            else:
                ans = 1+2*(d//l)
            print(ans)
    else:
        l *= -1
        if B1 > A1:
            print(0)
        else:
            d = (A1-B1)*T1
            if d%l == 0:
                ans = 2*(d//l)
            else:
                ans = 1+2*(d//l)
            print(ans)
    
if __name__ == "__main__":
    main()
