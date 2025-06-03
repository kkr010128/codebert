N = int(input())
S = input()
ans = 0
s = 0
while True:
    x = S.find('ABC', s)
    if x == -1:
        break
    else:
        s = x+1
        ans +=1

print(ans)