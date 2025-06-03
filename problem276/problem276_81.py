n = int(input())
li = list(map(int,input().split()))
s = sum(li)
sum_li = []
left = 0
right = s
for i,l in enumerate(li):
    if i == len(li)-1:
        break
    left += l
    right -= l
    sum_li.append(abs(left-right))
print(min(sum_li))