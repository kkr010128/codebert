n = int(input())
s = list(map(int, input().strip().split()))
befmax=0
sumlong=0
for i in range(0,n):
    if(befmax>s[i]):
        sumlong += befmax-s[i]
    else:
        befmax=s[i]

print(sumlong)