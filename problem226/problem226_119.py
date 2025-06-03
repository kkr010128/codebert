n1, n2 = [int(i) for i in input().split()]

n3 = [int(j) for j in input().split()]

for i1 in range(n2):
    n1 -= n3[i1]

if n1 <= 0:
    print("Yes")
else:
    print("No")