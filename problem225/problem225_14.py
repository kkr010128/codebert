H, A = map(int, input().split())
res = H//A
if H%A != 0 :
    res=res+1
print("{}".format(res))
