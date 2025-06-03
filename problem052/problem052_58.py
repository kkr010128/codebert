#coding: utf-8

n = int(input())

for i in range(1, n+1):
    x = i
    if x % 3 == 0:
        print(" " + str(x), end = '')
        continue
    

    for j in range(6):
        if int(x / (10**j)) % 10 == 3:
            print(" " + str(x), end = '')
            break
print("")
