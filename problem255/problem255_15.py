N = int(input())
S,T = input().split()
print(''.join([X+Y for (X,Y) in zip(S,T)]))