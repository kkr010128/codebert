
w1, w2 = input().split()
a,b = map(int,input().split())
c = input()
l = [[w1,a],[w2,b]]
ans = ""
for i in range(2):
    x,y = l[i][0],l[i][1]
    if x==c:
        ans += str(y-1)
    else:
        ans += str(y)
    if i==0:
        ans += ' '

print(ans)