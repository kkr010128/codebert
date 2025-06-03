n = int(input())
dic = {}
total = 0
for _ in range(n):
    s, t = input().split()
    total += int(t)
    dic[s] = total
x = input()
total -= dic[x]
print(total)