import sys
input = sys.stdin.readline

def main():
    N = int(input())
    ans = ''
    while N > 0:
        N -= 1
        ans += chr(ord('a') + N % 26)
        N = N // 26

    print(ans[::-1])

main()