N = int(input())
A = list(map(int, input().split()))

bitlist = [0] * 60

for i in A:
    for index, num in enumerate(reversed(bin(i)[2:])):
        if num == "1":
            bitlist[index] += 1
ans = 0
for bit, num in enumerate(bitlist):
    ans += num * (N-num) * (2 ** bit)
    ans %= (10**9+7)
print(ans)