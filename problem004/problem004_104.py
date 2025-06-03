n = int(input())
ans = list()

for i in range(n):
        line = input().split(" ")
        a = float(line[0])
        b = float(line[1])
        c = float(line[2])
        if ((a**2 + b**2) == c**2) or ((b**2 + c**2) == a**2) or ((c**2 + a**2) == b**2):
            ans.append("YES")
        else:
            ans.append("NO")

for j in range(n):
        print(ans[j])