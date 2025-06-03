n=int(input())
a=list(map(int,input().split()))
sum=[0]*(len(a)+1)
for i in range(len(a)):
    sum[i+1]=sum[i]+a[i]
# print(sum)

mini=2020202020
for i in range(len(sum)):
    mini=min(mini, abs(sum[i] - (sum[-1] - sum[i])))

print(mini)