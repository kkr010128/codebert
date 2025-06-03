n = int(input())
s = 100000

for i in range(n):
    s = int((s*1.05)/1000+0.9999)*1000

print(s)


