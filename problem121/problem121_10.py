def alp(c):
    return chr(c+64)

def Base10to(n,k):
    if(int(n/k)):
        if n%k ==0 and n/k==1:
            return str(alp(26))
        elif n%k ==0:
            return Base10to(int((n/k)-1),k)+str(alp(26))
        else:
            return Base10to(int(n/k),k)+str(alp(n%k))
    return str(alp(n%k))

n = int(input())
k = 26

ans = Base10to(n,k)
print(ans.lower())