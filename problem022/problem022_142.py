n = int(input())
s = input().split()
q = int(input())
t = input().split()
c = 0

for i in t:
    for j in s:
        if i == j:
            c += 1
            break
print(c)

