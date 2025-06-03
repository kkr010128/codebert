n = int(input())
ans = int(n/1.08)

for i in range(2):
    if int(ans*1.08) == n:
        print(ans)
        exit()
    ans += 1

print(":(")