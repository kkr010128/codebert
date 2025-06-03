input()
myarr = list(map(int, input().split()))
for i in range(len(myarr)):
    for j in range(i, 0,-1):
        if myarr[j] < myarr[j-1]:
            t = myarr[j]
            myarr[j] = myarr[j-1]
            myarr[j-1] = t
        else:
            break
    print(" ".join(map(str, myarr)))
        
    
