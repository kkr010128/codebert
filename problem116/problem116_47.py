s=str(input())
t=str(input())

n=len(s)
count=0

for i in range(n):
    if s[i]==t[i]:
        count+=1
    else:
        continue

print(n-count)
