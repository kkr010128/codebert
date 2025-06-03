num = input()
lst = []
for x in num:
    lst.append(int(x))

total = sum(lst)
if total % 9 == 0:
    print('Yes')
else:
    print('No')