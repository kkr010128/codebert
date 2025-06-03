n = int(input())
f = 100000
if n == 0:
    print(int(f))
else:
    for i in range(n):
        f *= 1.05
        #print(f)
        #F = f - f%1000 + 1000
        if f%1000 != 0:
            f = (f//1000)*1000 + 1000
            #print(i,f)
print(int(f))
