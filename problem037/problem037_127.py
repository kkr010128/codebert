L=[]
s=int(raw_input())
L+=divmod(s,3600)
L+=divmod(L[1],60)
print ("{0}:{1}:{2}").format(L[0],L[2],L[3])