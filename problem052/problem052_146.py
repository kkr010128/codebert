n = int(input())

result = ""
for i in (range(1,n+1)):
    if i % 3 == 0:
        result += " " + str(i)
        continue
    j = i
    while j > 0:
        if j % 10 == 3:
            result += " " + str(i)
            break
        else:
            j //= 10
        
       
print (result)
