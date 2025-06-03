s=input()
q=int(input())
mae=""
usr=""
flg=True
for i in range(q):    
    a=list(map(str,input().split()))
    if a[0]=="1":
        if flg:
            flg=False
        elif flg==False:
            flg=True
    if a[0]=="2":
        if a[1]=="1":
            if flg:
                mae=a[2]+mae
            else:
                usr=usr+a[2]
        if a[1]=="2":
            if flg:
                usr=usr+a[2]
            else:
                mae=a[2]+mae
if flg:
    ans=mae+s+usr
else:
    ans=usr[::-1]+s[::-1]+mae[::-1]
print(ans)