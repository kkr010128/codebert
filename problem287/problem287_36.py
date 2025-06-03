N=int(input())
resurt=''
for i in range(1,10):
    if N%i ==0 and N//i<=9: 
        result='Yes'
        break
    else:
        result='No'
print(result)