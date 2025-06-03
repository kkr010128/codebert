a,b,c=map(int,input().split())
d={"a":a,"b":b,"c":c}
for i in range(int(input())+1):
    if d["a"]<d["b"]<d["c"]:
        print("Yes")
        exit()
    elif d["a"]>=d["c"]: d["c"]*=2
    elif d["a"]>=d["b"]: d["b"]*=2
    elif d["b"]>=d["c"]: d["c"]*=2
print("No")
