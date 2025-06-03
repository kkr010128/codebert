N = int(input())
A = list(map(int,input().split()))

number_list = [0]*1000010
for a in A:
    number_list[a] += 1
    
flag1 = True
flag2 = True

for i in range(2,1000001):
    count = 0
    for j in range(1,1000001):
        if i*j > 1000000:
            break
        tmp = i*j
        count += number_list[tmp]
    if count > 1:
        flag1 = False
    if count == N:
        flag2 = False
        
if flag2 == False and flag1 == False:
    print("not coprime")
elif flag2 == True and flag1 == False:
    print("setwise coprime")
else:
    print("pairwise coprime")