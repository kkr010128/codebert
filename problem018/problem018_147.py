lst = raw_input().split()
lst2 = []
for v in lst:
    if v == "+":
        lst2[len(lst2)-2] += lst2.pop()
    elif v == "-":
        lst2[len(lst2)-2] -= lst2.pop()
    elif v == "*":
        lst2[len(lst2)-2] *= lst2.pop()
    elif v == "/":
        lst2[len(lst2)-2] /= lst2.pop()
    else:
        lst2.append(int(v))
print lst2[0]