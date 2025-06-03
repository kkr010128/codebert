n = int(input())
s = input()
ans = 0
for i in range(1000):
    i = str(i).zfill(3)
    ind = 0
    a = 0
    for ij in i:
        while(ind < len(s)):
            if s[ind] == ij:
                a += 1
                ind += 1
                break
            ind += 1
    ans += a == 3
print(ans)
