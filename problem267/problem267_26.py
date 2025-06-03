n = int(input())
s = list(input())
c = 0

for i in range(1000) :
    num_1 = i // 100
    num_2 = (i - num_1*100) // 10
    num_3 = (i - num_1*100 - num_2*10) % 100
    if str(num_1) not in s :
        continue
    if str(num_2) not in s :
        continue
    if str(num_3) not in s :
        continue
    for j in range(n-2) :
        if int(s[j]) == num_1 :
            for k in range(j+1,n-1) :
                if int(s[k]) == num_2 :
                    for l in range(k+1,n) :
                        if int(s[l]) == num_3 :
                            c += 1
                            break
                    break
            break

print(c)
