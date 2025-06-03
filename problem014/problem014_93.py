def bubbleSort(a, n):
    flag = True
    count = 0
    while flag:
        flag = False
        for j in range(1, n)[::-1]:
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                count += 1
                flag = True
    return count

def show(a, n):
    for i in range(n):
        if i == n-1:
            print "%d" % a[i]
        else:
            print "%d" % a[i],

n = input()
a = map(int, raw_input().split())
c = bubbleSort(a, n)
show(a, n)
print "%d" % c