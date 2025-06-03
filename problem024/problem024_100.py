n,k=map(int,input().split())
w=[0]*n
for i in range(n):
    w[i] = int(input())

def hantei(w,a,k):
    tumu=a
    daime=1
    for ww in w:
        if ww<=tumu:
            tumu-=ww
        else:        
            tumu=a
            daime+=1
            if ww<=tumu:
                tumu-=ww
            else:
                return False
    if daime >k:
        return False
    else:
        return True


right= max(w)*n +1
left = min(w)

while left<right:
    mid  = (left+right)//2
    if hantei(w,mid,k):
        right=mid
    else:
        left=mid+1
print(left)

