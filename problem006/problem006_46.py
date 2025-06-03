m = 100000
for i in range(int(raw_input())):
    m*=1.05
    m=(int((m+999)/1000))*1000

print m