N = int(input())
x = list(input())[::-1]
num = 0
nump = 0
numm = 0
pop_num = 0
for i in range(N):
        if x[i] == "1":
            pop_num += 1
for i in range(N):
    if x[i] == "1":
        num += pow(2,i,pop_num)
        num %= pop_num 
        nump += pow(2,i,pop_num+1)
        nump %= pop_num  + 1
        if pop_num-1 != 0:
            numm += pow(2,i,pop_num - 1)
            numm %= pop_num - 1



def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

x = x[::-1]
def calc(i,depth,n):
    if depth == 0:
        if x[i] == "1":
            tmp = numm
            if pop_num - 1 != 0:
                tmp -= pow(2,N-i-1,pop_num-1)
                tmp %= (pop_num - 1)
            else:
                return 0
            return calc(i,depth+1,tmp)
        else:
            tmp = nump
            tmp += pow(2,N-i-1,pop_num+1)
            tmp %= (pop_num + 1)
            return calc(i,depth+1,tmp)
    else:
        if n == 0: return depth
        return calc(i,depth+1, n % popcnt(n))
        

for i in range(N):
    print(calc(i,0,0))

