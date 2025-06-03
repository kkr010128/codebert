K = int(input())

def make(i):
    if int(i) > 3234566667:  return
    lun.append(int(i))
    if i[-1] == "0":
        temp = i + "0"
        make(temp)
        temp = i + "1"
        make(temp)
    elif i[-1] == "9":
        temp = i + "8"
        make(temp)
        temp = i + "9"
        make(temp) 
    else:
        temp = i + str(int(i[-1]) - 1)
        make(temp)
        temp = i + i[-1]
        make(temp)   
        temp = i + str(int(i[-1]) + 1)
        make(temp)
        
lun = []
for i in range(1, 10):
    make(str(i))
lun = sorted(lun)
ans = lun[K - 1]
print(ans)