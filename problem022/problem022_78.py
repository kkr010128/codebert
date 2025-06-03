n = int(input()); s = input().split()
q = int(input()); t = input().split()
cnt = 0
for i in t:
    if i in s:
        cnt += 1
print(cnt)

