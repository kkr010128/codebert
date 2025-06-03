n = int(input())
iteration = n
ex = 0
count = 0
for i in range(1,n):
    ex = iteration-i
    #print(ex)
    if ex <=i:
        break
    else:
        count += 1
print(count)