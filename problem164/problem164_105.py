# coding: utf-8

def main():
    a, b, c, d = map(int, input().split())
    for _ in range(100):
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <=0:
            print("No")
            break

main()
