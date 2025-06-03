n,m = map(int,input().split())
li = list(map(int,input().split()))
sum_vote = sum(li)
kijun = sum_vote / (4 * m)
sum_above = len([i for i in li if i >= kijun])
if sum_above >= m:
    print("Yes")
else:
    print("No")

