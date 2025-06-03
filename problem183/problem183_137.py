n=int(input())

def m_div(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def check(num,k):
    if k==1:
        return False

    while num>=k:
        if num%k==0:
            num=num//k
        else:
            break
    num%=k
    return num==1

n1divs = m_div(n-1)
ndivs  = m_div(n)

ans=[]
for num in n1divs:
    if check(n,num):
        ans.append(num)
for num in ndivs:
    if check(n,num):
        ans.append(num)
print(len(set(ans)))