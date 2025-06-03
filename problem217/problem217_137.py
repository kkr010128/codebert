#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))

n = int(input())
a = list(map(int, input().split()))

ans = "APPROVED"
for i in range(n):
    if (a[i] % 2 == 0):
        if (a[i] % 3 == 0 or a[i] % 5 == 0):
            pass
        else:
            ans = "DENIED"
            break
print(ans)
