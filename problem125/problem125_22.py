x = int(input())

n=1

while 1:
    angle_n = 360*n
    if angle_n % x == 0:
        ans = angle_n // x
        break
    else:
        n += 1

print(ans)