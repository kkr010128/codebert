tmp = input().split()
a = int(tmp[0])
b = int(tmp[1])
c = int(tmp[2])
ans = 0
if a == b:
    if c % a == 0:
        ans += 1
else:
    for n in range(a,b + 1):
        if c % n == 0:
            ans +=1
        else:
            pass
print(ans)

