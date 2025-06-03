a,b = map(int, open(0).read().split())

i = int(a/0.08-1e-8)
while 1:
    if int(i*0.08)==a and int(i*0.1)==b:
        print(i)
        break
    if int(i*0.08)>a:
        print(-1)
        break
    i += 1