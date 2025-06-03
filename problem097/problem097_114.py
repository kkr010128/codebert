import sys
def main():
    k = int(input())

    a =7%k
    if a == 0:
        print(1)
        sys.exit()

    for i in range(2,10**7):
        a = (10*a+7) % k
        if a == 0:
            print(i)
            sys.exit()

    print(-1)
    
main()