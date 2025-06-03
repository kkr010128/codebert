# coding: utf-8
# Your code here!

H=int(input())
count=0
ans=0
while H>1:
    H=H//2
    count+=1
for i in range(count+1):
    ans+=2**i
print(ans)