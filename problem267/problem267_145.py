n = int(input())
S = input()
ans = 0
def ok(i):
    pin = '{:0=3}'.format(i)
    j = 0
    for s in S:
        if s == pin[j]:
            j += 1
            if j == 3:
                return True
    else:
        return False

for i in range(1000):
    ans += ok(i)
print(ans)