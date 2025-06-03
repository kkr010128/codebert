N = input()
l = map(int, raw_input().split())
i = 1
while i < N:
    l_str = map(str,l)
    print " ".join(l_str)
    tmp = l[i]
    j = i - 1
    while j >= 0 and tmp < l[j]:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = tmp
    i += 1
l_str = map(str,l)
print " ".join(l_str)