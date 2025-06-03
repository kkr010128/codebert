n = int(input())
ans = []
while(n > 0):
    x = n %  26
    n = n // 26
    if(x == 0):
        x = 26
        n -= 1
    ans.append(chr(x + ord('a') -1))
    # print(x,n)
ans.reverse()
print("".join(ans))
