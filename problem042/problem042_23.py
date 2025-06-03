a = []
for i in range(10000):
    a.append(int(input()))
    if a[i] == 0:
        break
    print("Case {}: {}".format(i+1,a[i]))
