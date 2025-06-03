input()
s = input().split()
input()
t = input().split()

cnt = 0

for t1 in t:
    for s1 in s:
        if t1 == s1:
            cnt += 1
            break

print(cnt)