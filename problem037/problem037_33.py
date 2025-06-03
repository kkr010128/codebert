#hは時間,mは60未満の分,sは60未満の秒
S=int(input())
h=int(S/3600)
m=int(S%3600/60)
s=int(S%3600%60)
print(str(h)+":"+str(m)+":"+str(s))
