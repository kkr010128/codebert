x, k, d = map(int,input().split())
x = abs(x)
if x>k*d:
    ans = x-k*d
else:
    cnt = x//d#xに最も近づくための移動回数
    if (k-cnt)%2==0:
        ans = x-cnt*d
    else:
        if x>0:
            ans = abs(x-cnt*d-d)
        else:
            ans = abs(x-cnt*d+d)
print(ans)