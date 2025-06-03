numberOfArray=int(input())
arrayList=list(map(int,input().split()))

def bubbleSort():
    frag=1
    count=0
    while frag:
        frag=0
        for i in range(1,numberOfArray):
            if arrayList[i-1]>arrayList[i]:
                arrayList[i-1],arrayList[i]=arrayList[i],arrayList[i-1]
                frag=1
                count+=1
    arrayForReturn=str(arrayList[0])
    for i2 in range(1,numberOfArray):
        arrayForReturn+=" "+str(arrayList[i2])
    print(arrayForReturn)
    print(count)

#------------------main--------------
bubbleSort()
