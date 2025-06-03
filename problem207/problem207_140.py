A11, A12, A13 = map(int, input().split())
A21, A22, A23 = map(int, input().split())
A31, A32, A33 = map(int, input().split())
N = int(input())
B = {int(input()) for _ in range(N)}

h1 = {A11, A12, A13}
h2 = {A21, A22, A23}
h3 = {A31, A32, A33}
v1 = {A11, A21, A31}
v2 = {A12, A22, A32}
v3 = {A13, A23, A33}
c1 = {A11, A22, A33}
c2 = {A13, A22, A31}

if len(h1 & B)==3 or len(h2 & B)==3 or len(h3 & B)==3 or len(v1 & B)==3 or len(v2 & B)==3 or len(v3 & B)==3 or len(c1 & B)==3 or len(c2 & B)==3:
    print("Yes")
else:
    print("No")

