








def     process(tab, first, end):
    #print(tab)
    #print(first, end)
    total = first
    for i in tab:
        if (i[1] > total):
            return ("No")
        total += i[0]
        if (total < 0):
            return ("No")
    if (total == end):
        return ("Yes")
    return ("No")




N  = int(input())

first = 0
last = 0
clean = 0
tab = []
total = 0
for i in range(N):
    s = input()
    avant = 0
    apres = 0
    for j in s:
        if (j == '('):
            apres += 1
        elif (j == ')'):
            if (apres > 0):
                apres -= 1
            else:
                avant += 1
    if (avant == 0 and apres > 0):
        first += apres
    elif (apres == 0 and avant > 0):
        last += avant
    elif (avant > 0 or apres > 0):
        tab.append((apres - avant, avant, apres, s))
    else:
        clean += 1
    total += avant - apres
if (first == -1 and clean > 0):
    first = 0
    clean -= 1
if (last == -1 and clean > 0):
    last = 0


tab = sorted(tab)
tab = tab[::-1]
if (total == 0 and first > -1 and last > -1):
    res = process(tab, first, last)
else:
    if (total == 0 and N == 1):
        res = "Yes"
    else:
        res = "No"
print(res)
