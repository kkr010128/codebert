n = int(input())
a = 0
for i in range(n+1):
    if i%3== 0: continue
    elif i%5 == 0:continue
    elif i%3 ==0 and i %5 ==0:continue
    else: a+=i

print(a)