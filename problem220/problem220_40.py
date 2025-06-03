S,T = (input().split())
A,B = (int(i) for i in input().split())
U = input()


if S == U :
    A = A - 1
elif T == U:
    B = B - 1
    
print(A,B)
