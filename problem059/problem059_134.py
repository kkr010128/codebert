all_ele = []
sum_ele = []
h,w = [int(x) for x in input().split()]
for ele in range(h):
    all_ele.append([int(x) for x in input().split()])
    all_ele[ele].append(sum(all_ele[ele]))
    
all_ele.append([int(x) for x in range(w+1)])

for a in range(len(all_ele[0])):
    for b in range(h):
        sum_ele.append(all_ele[b][a])
    all_ele[h][a] = sum(sum_ele)
    sum_ele = []
    
for out1 in all_ele:
    print(' '.join(map(str,out1)))
