
def Li():
    return list(map(int, input().split()))


N = int(input())
A = Li()

ans = 1
if 0 in A:
    ans = 0
else:
    for i in A:
        ans *= i
        if ans > pow(10, 18):
            ans = -1
            break
print(ans)
