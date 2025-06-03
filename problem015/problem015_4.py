N = int(raw_input())
lst = map(int, raw_input().split())
cnt = 0
for i in range(0, len(lst)):
    m = i
    for j in range(i, len(lst)):
        if lst[m] > lst[j]:
            m = j
    if m != i:
        lst[i], lst[m] = lst[m], lst[i]
        cnt+=1

print " ".join(map(str,lst))
print (cnt)