n = int(input())

list_s = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list_h = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list_c = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list_d = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in range(n):
    zugara, num = input().split()
    #print(zugara)
    #print(num)
    #print(list_s)
    if zugara == 'S':
        list_s.remove(int(num))
    elif zugara == 'H':
        list_h.remove(int(num))
    elif zugara == 'C':
        list_c.remove(int(num))
    else:
        list_d.remove(int(num))

for i in list_s:
    print('S', i)
for i in list_h:
    print('H', i)
for i in list_c:
    print('C', i)
for i in list_d:
    print('D', i)
