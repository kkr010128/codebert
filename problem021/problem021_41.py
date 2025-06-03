S = input()

l1 = []
l2 = []
total_area = 0
for i, j in enumerate(S):
    if j == '\\':
        l1.append(i)
    elif j == '/' and l1:
        i_p = l1.pop()
        v = i -i_p
        total_area += v
    
        while l2 and l2[-1][0] > i_p:
            v += l2.pop()[1]
        l2.append([i_p, v])
        
ans = [str(len(l2))] + [str(k[1]) for k in l2]
print(total_area)
print(' '.join(ans))
