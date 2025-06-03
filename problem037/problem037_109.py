S = int(input())
h = int(S/3600)
m = int((S- h*3600)/60)
sec = S- h*3600-m*60;
print(str(h)+":"+str(m)+":"+str(sec))
