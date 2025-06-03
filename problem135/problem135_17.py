# coding: utf-8
# Your code here!
import math

def main():
    A, B = input().split()
    B = int(B.replace(".",""))
    ans = int(A) * B // 100 
    print(ans)

main()