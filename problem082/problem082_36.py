
st1 = input()
st2 = input()
li = []
count = 0

k = 0

for i in range(len(st1)-len(st2)+1):
    for s2 in st2:
        if s2 in st1[i+k]:
            count += 1
        k += 1
    li.append(count)
    count = 0
    k = 0

print(len(st2) - max(li))
