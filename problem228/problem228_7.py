c= int(input())
ans =0
s = 0

while c >1:
    c = c//2
    ans += 1

for i in range(1,ans+1):
    s += 2**i

print(s+1)