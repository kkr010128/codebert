n = int(input())
s = input()

r = set([i+1 for i in range(n) if s[i] == "R"])
g = set([i+1 for i in range(n) if s[i] == "G"])
b = set([i+1 for i in range(n) if s[i] == "B"])
ans = len(r)*len(g)*len(b)


def check(s1, s2, s3):
    t = 0
    for i in range(1, n+1):
        if not i in s1:
            continue
        for j in range(i+1, n+1):
            if not j in s2:
                continue
            if (j+(j-i)) in s3:
                t += 1
    return t


ans -= check(r, g, b)
ans -= check(r, b, g)
ans -= check(g, b, r)
ans -= check(g, r, b)
ans -= check(b, r, g)
ans -= check(b, g, r)
print(ans)
