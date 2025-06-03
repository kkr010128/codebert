###綺麗になったよ！！！！！
def y_solver(tmp):
    l=len(tmp)
    rev=tmp[::-1]+"0"
    ans=0
    next_bit=0
    kuri_cal=0
    for i in range(l-1):
        num=int(rev[i])+next_bit
        next_num=int(rev[i+1])
        if (num<5) or (num==5 and next_num<5):
            ans+=(kuri_cal+num)
            kuri_cal=0
            next_bit=0
        else:
            kuri_cal+=10-num
            next_bit=1 
    
    last=int(tmp[0])+next_bit
    ans+=kuri_cal+min(last,11-last)
    return ans

n=input()
ans=y_solver(n)
print(ans)