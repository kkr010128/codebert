n = int(input())
dic = {}
for i in range(n):
    req = input().split()
    if(req[0] == "insert"):
        dic[req[1]] = i
    elif(req[0] == "find"):
        if(req[1] in dic):
               print("yes")
        else:
               print("no")
