def check(st):
    for d in range(len(st)):
        if st[d]=="3":
            return True
    return False

num = int(input())
str=""
for d in range(3,num+1):
    s = "%d"%(d)
    if d%3==0 or check(s):
        str+=" %d"%(d)
print(str)