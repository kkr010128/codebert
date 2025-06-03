a = int(input())
b = a - int(a / 3600)*3600
c = b - int(b / 60)*60
print(str(int(a/3600))+":"+str(int(b/60))+":"+str(int(c)))
