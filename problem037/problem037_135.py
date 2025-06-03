S = int(input())
s = S%60
m = (S-s)/60%60
h = S/3600%24
answer = str(int(h))+":"+str(int(m))+":"+str(s)
print(answer)

