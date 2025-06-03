data = set()
for i in range(1,10):
    for j in range(1,10):
        data.add(i*j)
if int(input()) in data:
    print("Yes")
else:
    print("No")