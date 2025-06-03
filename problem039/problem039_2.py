n = input().split()
n_int = list(map(int,n))
a = n_int[0]
b = n_int[1]
c = n_int[2]

if a < b < c:
    print("Yes")
else:
    print("No")