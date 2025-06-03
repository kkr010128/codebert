n = input()
a = [raw_input() for _ in range(n)]
b = []
for i in ['S ','H ','C ','D ']:
    for j in range(1,14):
        b.append(i+str(j))
for i in a:
    b.remove(i)
for i in b:
    print i