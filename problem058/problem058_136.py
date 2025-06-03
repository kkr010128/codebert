ele_and_tar = []
rs = []
flag1 = 1
flag2 = 0
while flag1:
    data = [int(x) for x in input().split()]
    if data == [0,0]:
        flag1 = 0
    else:
        ele_and_tar.append(data)
        
for i in range(len(ele_and_tar)):
    rs.append(0)
for math in ele_and_tar:
    for i in range(1,math[0]+1):
        for j in range(i+1,math[0]+1):
            for k in range(j+1,math[0]+1):
                if (i + j + k) == math[1]:
                    rs[flag2] = rs[flag2] + 1
    flag2 = flag2 + 1
    
for out in rs:
    print(out)

