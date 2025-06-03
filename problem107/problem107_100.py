def popcount_int(n):
    return bin(n).count('1')

def popcount_bin(s):
    return s.count('1')

def poptimes(n,cnt=1):
    if n==0:
        return cnt
    else:
        n%=popcount_int(n)
        cnt+=1
        return poptimes(n,cnt)

N=int(input())
S=input()

S_int=int(S,2)
pc=popcount_bin(S)
pc_plus=S_int%(pc+1)
if pc!=1:
    pc_minus=S_int%(pc-1)

for i in range(N):
    if S[i]=='1':
        if pc!=1:
            tmp=pc_minus-pow(2,N-i-1,pc-1)
            print(poptimes(tmp%(pc-1)))
        else:
            print(0)
            continue
    else:
        tmp=pc_plus+pow(2,N-i-1,pc+1)
        print(poptimes(tmp%(pc+1)))