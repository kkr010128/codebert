import sys

def selection_sort(x):
    count = 0
    for i in range(0,len(l)-1):
        mini = i
        for j in range(i+1,len(l)):
            if(x[j] < x[mini]):
                mini = j
        if(mini != i):
            count += 1
            temp = x[i]
            x[i] = x[mini]
            x[mini] = temp
    for data in x:
        print data,
    print
    print count


l = []
for input in sys.stdin:
    l.append(input)
l = l[1:]
l = l[0].split()
for i in range(0,len(l)):
    l[i] = int(l[i])
selection_sort(l)
