x,y = map(int,input().split())
s = max(0,(4-x)*100000)+max(0,(4-y)*100000)
print(s if s!=600000 else s+400000)