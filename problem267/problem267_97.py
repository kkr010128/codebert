n = int(input())
s = input()

ans = 0
for i in range(10):
    if str(i) in s:
        index_i = s.index(str(i))
        for j in range(10):
            if str(j) in s[index_i + 1:]:
                index_j = s[index_i + 1:].index(str(j)) + index_i + 1
                for k in range(10):
                    if str(k) in s[index_j + 1:]:
                        ans += 1
print(ans)