from sys import stdin
def make_divisors(n):
    mod0 = set()
    mod1 = set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            mod0.add(i)
            mod0.add(n/i)
        if (n-1)%i==0:
            mod1.add(i)
            mod1.add((n-1)/i)
    return mod0,mod1

N=list(map(int,(stdin.readline().strip().split())))

num=N[0]
if num==2:print(1)
else:
    K=0
    mod0,mod1=(make_divisors(num))
    # mod0.remove(1)
    # mod1.remove(1)
    for i in mod0:
        num = N[0]
        while(num % i == 0):
            num/=i

        if num%i==1:
            K+=1
    K+=len(mod1)+2
    print(K)
