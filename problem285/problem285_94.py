s=input()
#><となるところを見つける<<となるところを見つける>>となるところを見つける<>となるところについて考える
n=len(s)
ans=[0]*(n+1)

#左から>>となる部分を探す
for i in range(n):
    if s[i]=='<':
        ans[i+1]=max(ans[i+1],ans[i]+1)

for i in reversed(range(n)):
    if s[i]=='>':
        ans[i]=max(ans[i],ans[i+1]+1)
print(sum(ans))
#rangeの挙動に注意しよう