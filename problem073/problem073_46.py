import sys
def input(): return sys.stdin.readline().rstrip()
def main():
    n = int(input())
    ans = 0
    for a in range(1,n):
        if a ** 2 >= n:
            break
        for b in range(a,n):
            if a * b >= n:
                break
            if a == b:
                ans += 1
            else:
                ans += 2
    print(ans)
        

if __name__=='__main__':
    main()