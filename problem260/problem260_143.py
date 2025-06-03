import sys
input = sys.stdin.readline

A = list(map(int, input().split()))

if sum(A) >= 22:
    print('bust')
else:
    print('win')
    
