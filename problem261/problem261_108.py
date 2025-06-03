s = input()

iters = len(s) // 2

count=0
for i in range(iters):
    if s[i] != s[-(i+1)]:
        count+=1


print(count)