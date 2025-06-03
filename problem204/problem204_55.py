s = list(input())

q = int(input())

before = []

after = []

cnt = 0

for i in range(q):
    t = list(input().split())
    
    if t[0] == "1":
        cnt += 1
    else:
        f = t[1]
        c = t[2]
        if f == "1":
            if cnt%2 == 0:
                before.append(c)                      
            else:
                after.append(c)
        else:
            if cnt%2 == 0:
                after.append(c)
            else:
                before.append(c)
                
if cnt%2 == 1:
    s.reverse()
    after.reverse()
    #before.reverse()
    for i in after:
        print(i,end = "")
    for i in s:
        print(i,end = "")
    for i in before:
        print(i,end = "")
else:
    before.reverse()
    before.extend(s)
    before.extend(after)
            
    for i in before:
        print(i,end = "")