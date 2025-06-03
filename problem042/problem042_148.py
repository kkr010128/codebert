list = []
while True:
    a = int(input())
    if(a == 0): break
    else: list.append(a)
    

for i in range(len(list)):
    print("Case %d: %d" %(i+1,list[i]))
