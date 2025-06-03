n = int(input())
a = list(map(int,input().split()))
largest = max(a)
b = [True] * (largest+1)
dict = {}
ans = 0
for num in a:
    if num in dict.keys():
        b[num] = False
    else:
        dict[num] = 1
        y = num * 2
        while(y <= largest):
            b[y] = False
            y += num
for num in a:
    if b[num] == True:
        ans += 1
print(ans)