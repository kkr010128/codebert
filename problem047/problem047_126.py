listA=[]
listOP=[]
listB=[]
count=0
while True:
    a,op,b=input().split()
    listA.append(int(a))
    listOP.append(op)
    listB.append(int(b))
    if op=="?":
        del listA[len(listA)-1]
        del listOP[len(listOP)-1]
        del listB[len(listB)-1]
        break
#入力パートここまで。計算出力パートここから
while count<=len(listA)-1:
    if listOP[count]=="+":
        print(listA[count]+listB[count])
    elif listOP[count]=="-":
        print(listA[count]-listB[count])
    elif listOP[count]=="*":
        print(listA[count]*listB[count])
    elif listOP[count]=="/":
        print(listA[count]//listB[count])
    else:
        print("ERROR")
    count+=1
