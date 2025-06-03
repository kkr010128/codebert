n = int(input())
mydict = {}
answer_list = []

for i in range(n) :
    query, wd = input().split()
    
    if query == "insert" :
        mydict[wd] = 1
    else :
        if wd in mydict.keys() : answer_list.append("yes")
        else : answer_list.append("no")
        
for i in answer_list :
    print(i)
