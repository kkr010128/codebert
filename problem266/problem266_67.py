x = int(input())

flag = 0
if x >= 2000:
    print(1)
    exit()
else:
    for i in range(20):
        for j in range(20):
            for k in range(20):
                for l in range(20):
                    for m in range(20):
                        for n in range(20):
                            if i*100+j*101+k*102+l*103+m*104+n*105 == x:
                                flag = 1
                                print(1)
                                exit()
if flag != 1:
    print(0)