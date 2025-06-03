N = int(input())
a = []
for i in range(N):
    a = list(map(int, input().split()))
 
    side_a = a[0]
    side_b = a[1]
    side_c = a[2]
    if side_a ** 2 + side_b ** 2 == side_c ** 2 \
        or side_c ** 2 + side_b ** 2 == side_a ** 2 \
        or side_a ** 2 + side_c ** 2 == side_b ** 2:
        print("YES")
    else:
        print("NO")