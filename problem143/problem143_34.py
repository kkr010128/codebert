k=int(input())
s=str(input())
long =len(s)
i =0
ans = str()
if k>long:
    print(s)
else:
    for i in range(long):
        if i<k:
           ans = str(ans+s[i])
        else:
           ans = str(ans+"...")
           break
print(ans)