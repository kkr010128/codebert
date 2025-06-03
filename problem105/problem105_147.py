numb=input()
inputs = list(map(int,input().split()))
count=0
for i in range(0,len(inputs)):
    if ((i+1)%2!=0) and ((inputs[i]%2)!=0):
        count+=1
    
print(count)    