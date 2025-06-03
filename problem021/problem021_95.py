S=input()
sum_a = 0
index = []
area = []
pos = []
for i,s in enumerate(S):
    if(s=="\\"):
        index.append(i)
    if(s=="/" and index):
        tmp = i - index[-1]
        sum_a += tmp
        pop = index.pop()
        while pos and pop < pos[-1]:
            tmp += area.pop()
            pos.pop()
        pos += [pop]
        area += [tmp]
        
print(sum_a)
print(len(area),*(area))