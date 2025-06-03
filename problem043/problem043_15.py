def swap(a, b ,item):
    c = item[a]
    item[a] = item[b]
    item[b] = c
    
AB = input().split()
a = int(AB[0])
b = int(AB[1])
while a!=0 or b!=0:
    if a>b:
        swap(0, 1, AB)
    print(int(AB[0]), int(AB[1]))
    AB = input().split()
    a = int(AB[0])
    b = int(AB[1])