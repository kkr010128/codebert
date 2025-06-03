num = int(input())

hh = num // 3600
h2 = num % 3600

mm = h2 // 60
ss = h2 % 60

print(str(hh)+":"+str(mm)+":"+str(ss))

