N = int(input())
S = input()
NUMS = list(map(int, S))
ans = 0
for i in range(10):
    for j in range(10):
        iok = False
        jok = False
        k = set()
        for num in NUMS:
            if jok:
                k.add(num)
            elif iok:
                if num == j:
                    jok = True
            else:
                if num == i:
                    iok = True
        ans += len(k)
print(ans)