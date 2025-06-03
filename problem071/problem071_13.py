s=input()
l=len(s)
list_s=list(s)
ans=""
if(s[l-1]!="s"):
    list_s.append("s")
elif(s[l-1]=="s"):
    list_s.append("es")

for i in range(0,len(list_s)):
    ans+=list_s[i]

print(ans)