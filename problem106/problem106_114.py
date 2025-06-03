N = int(input())
x = y = z = 1
ans = [0]*N
while True:
    if x**2 + y**2 + z**2 + x*y + y*z + z*x > N:
        break
    while True:
        if x**2 + y**2 + z**2 + x*y + y*z + z*x > N:
            break
        while True:
            a = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if a <= N:
                if x != y and y != z and z != x:
                    ans[a-1] += 6
                elif x == y and y == z:
                    ans[a-1] += 1
                else:
                    ans[a-1] += 3
                z += 1
            else:
                break
        y += 1
        z = y
    x += 1
    z = y = x
for n in ans:
    print(n)