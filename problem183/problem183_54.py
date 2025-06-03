def make_divisors(n):
    div=[n]
    for i in range(2,-int(-n**0.5//1)):
        if n%i==0:
            div.append(i)
            div.append(n//i)
    if n%(n**0.5)==0:
        div.append(int(n**0.5))
    div.sort()
    return div

n=int(input())
if n>2:
    ans=make_divisors(n-1)
else:
    ans=[]
for i in make_divisors(n):
    a=n
    while a%i==0:
        a=a//i
    if a%i==1:
        ans.append(i)
print(len(ans))