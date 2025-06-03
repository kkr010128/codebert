from sys import stdin
import sys
##  input functions for me
def ria(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    N = ri()
    if N % 2 == 0:
        print(N // 2 - 1)
    else:
        print(N // 2)


if __name__ == "__main__":
    main()
