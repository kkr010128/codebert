N=int(input())
lis=[chr(i) for i in range(97, 97+26)]
ans=''
while N>0:
    N-=1
    ans+=lis[N%26]
    N=N//26
print(ans[::-1])