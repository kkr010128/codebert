k=raw_input().split()
k=raw_input().split()
k.sort()
for i in range(len(k)):
        k[i]=int(k[i])
        k.sort()
print min(k),
print max(k),
print sum(k)