n = input()
i = 1
num = []
while i <= n:
    if i % 3 == 0:
        num.append(i)
        i +=1
    else:
        x = i
        while x > 0:
            if x % 10 == 3:
                num.append(i)
                break
            else:
                x /=  10                
        i += 1
print("{}".format(str(num)).replace("["," ").replace("]","").replace(",",""))