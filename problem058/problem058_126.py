def solve(sup,rest,digit,used1,used2):
    if rest<0:
        return 0
    if digit==0:
        if rest==0:
            return 1
        else:
            return 0
    sum=0
    for i in range(1,sup+1):
        if i!=used1 and i!=used2:
            if used1==0:
                sum+=solve(sup,rest-i,digit-1,i,used2)
            elif used2==0:
                sum+=solve(sup,rest-i,digit-1,used1,i)
            else:
                sum+=solve(sup,rest-i,digit-1,used1,used2)
    return sum

N=[]
X=[]
while True:
    n,x=map(int,raw_input().split())
    if (n,x)==(0,0):
        break
    N.append(n)
    X.append(x)
for i in range(len(N)):
    print('%d'%(solve(N[i],X[i],3,0,0)/6))