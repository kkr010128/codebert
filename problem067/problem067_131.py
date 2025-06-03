taro,hanako = 0,0
w=[]
n = int(raw_input())
for i in xrange(n):
    w.append(map(str, raw_input().split()))
for j in xrange(n):
    if w[j][0]>w[j][1]:
        taro+=3
    elif w[j][0]<w[j][1]:
        hanako+=3
    else:
        taro+=1
        hanako+=1
#print n
#print w
print taro,hanako