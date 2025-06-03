s=input()
s_list=list(s)
 
x=len(s_list)

if s_list[x-1]=="s":
  s_list.append("es")
else:
  s_list.append("s")

print("".join(s_list))