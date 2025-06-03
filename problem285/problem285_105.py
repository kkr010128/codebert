s = input()
l = len(s)
lst = [0] * (l+1)

for idx in range(l):
    if s[idx] is '<':
        lst[idx+1] = max(lst[idx+1], lst[idx]+1)

for inv in range(1, l+1):
    if s[-inv] is '>':
        lst[-(inv+1)] = max(lst[-(inv+1)], lst[-inv]+1)


print(sum(lst))