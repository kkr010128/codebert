i=0
xArray=[]
yArray=[]
while True:
    x,y=(int(num) for num in input().split())
    if x==0 and y==0:
        break
    else:
        xArray.append(x)
        yArray.append(y)
        i+=1
for count in range(i):
    if xArray[count] < yArray[count]:
        print(xArray[count],yArray[count])
    else:
        print(yArray[count],xArray[count])
