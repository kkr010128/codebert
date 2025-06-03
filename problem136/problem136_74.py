n = int(input())

fact={}
i = 2
while n != 1:
    if n % i == 0:
        n = n/i
        if i in fact:
            fact[i] += 1
        else:
            fact[i] = 1
    else:
        i += 1
    if i > (n**(1/2)+1):
        if n in fact:
            fact[n] += 1
        else:
            fact[n] = 1
        break

if fact == {}:
    print(0)
else:
    ans = 0
    for v in fact.values():
        #print(v)
        for i in range(1,v+1):
            if v - i >= 0:
                ans +=1
                v = v-i
    print(ans)