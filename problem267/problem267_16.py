n = int(input())
s = input()
ans = 0

for i in range(1000):
        i = '0' * (3 - len(str(i))) + str(i)
        keep = 0

        for j in range(n):
                if s[j] == i[keep]:
                        keep += 1
                if keep == 3:
                        ans += 1
                        break

print(ans)
