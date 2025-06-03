n = int(input())
ans = ""
for i in range(11):
    n2 = (n-1)%26
    ans = chr(97+n2)+ans
    n = int((n-1)/26)
    #print(n)
    if n == 0:
        break
print(ans)    
