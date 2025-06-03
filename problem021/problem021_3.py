inputs = list(input())
stack = []
L = []
tmp_total = 0
counter = 0
upper = 0
for i,x in enumerate(inputs):
    if(x == '\\'):
        stack.append(i)
    elif(x == '/') and stack:
        tmp = stack.pop()
        total_layer = i-tmp
        if L:
            while L and L[-1][0] > tmp:
                cal = L.pop()
                total_layer += cal[1]
        L.append((i, total_layer))

print(sum([j[1] for j in L]))
if(len(L) != 0):
    print(str(len(L))+ ' ' + ' '.join([str(i[1]) for i in L]))
else:
    print(str(len(L)))

