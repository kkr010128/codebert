n=int(input())
li=[input() for i in range(n)]
ans=[0,0,0,0]
for i in range(n):
    if li[i]=="AC":
        ans[0]+=1
    elif li[i]=="WA":
        ans[1]+=1
    elif li[i]=="TLE":
        ans[2]+=1
    elif li[i]=="RE":
        ans[3]+=1
print("AC x " + str(ans[0]))
print("WA x "+ str(ans[1]))
print("TLE x "+str(ans[2]))
print("RE x "+str(ans[3]))