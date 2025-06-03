num = map(int, raw_input().split())

flg=1
while flg==1:
    flg=0
    for i in range(2):
        if num[i]>num[i+1]:
            box = num[i]
            num[i]=num[i+1]
            num[i+1]=box
            flg=1

print "%d %d %d" % (num[0],num[1],num[2])