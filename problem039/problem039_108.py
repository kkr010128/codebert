a = raw_input()
a = a.split()
for i in range(0,len(a)):
    a[i] = int(a[i])
b = sorted(a)
for i in range(0,len(a)):
    if(a[i] != b[i] or (i != (len(a) - 1) and a[i] == a[i+1])):
        print 'No'
        break
if(i == len(a)-1):
    print 'Yes'
