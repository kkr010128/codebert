S, T = [i for i in input().split()]
A, B = map(int, input().split())
U = input()
if U == S:
    A -= 1
elif U == T:
    B -= 1
print(str(A) + " " + str(B))
