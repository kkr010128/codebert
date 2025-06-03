#Is it Right Triangre?

n = int(input())
for i in range(n):
    set = input(). split()
    set = [int(a) for a in set] #int?????????
    set.sort()
    if set[0] ** 2 + set[1] ** 2 == set[2] ** 2:
        print("YES")
    else:
        print("NO")