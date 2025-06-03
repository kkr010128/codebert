import sys
input = sys.stdin.readline

def main():
    K = int(input())

    t = 7
    t %= K
    for i in range(K+1):
        if t == 0:
            print(i+1)
            break
        t = (t * 10 + 7) % K
    else:
        print(-1)
    

main()