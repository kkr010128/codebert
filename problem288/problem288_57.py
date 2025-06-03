#nの約数を列挙する関数
import math
def n_div(n):
    div_list = []
    import math
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if n % i ==0:
            div_list.append(i)
            if i*i ==n:
                continue
            div_list.append(n//i)
    div_list.sort()
    return div_list

n = int(input())
lr = n_div(n)
#print(lr)
if len(lr) % 2==0:
    a = len(lr)/2
    a = int(a)
    ans = lr[a]+lr[a-1]-2
else:
    a = math.floor(len(lr)/2)
    #print(a)
    ans = lr[a]*2  -2
    
print(ans)