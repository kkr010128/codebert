integers=[]
i=0
j=0
while True:
    num=int(input())
    integers.append(num)
    if integers[i]==0:
        del integers[i]
        break
    i+=1
while j<i:
    print('Case {}: {}'.format(j+1,integers[j]))
    j+=1
