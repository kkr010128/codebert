n = int(input())
n_ = n-1
a = [n]
if n_ == 1:
    a_ = []
else:
    a_ = [n_]
    
for i in range(2,int(n**0.5//1+1)):
    if n%i == 0:
        a.append(i)
        if n/i != i:
            a.append(n/i)
    if n_%i == 0:
        a_.append(i)
        if n_/i != i:
            a_.append(n_/i)

ans = len(a_)
for i in a:
    num = n
    while num%i == 0:
        num /= i
    if num % i == 1:
        ans += 1
    
print(ans)