N = int(input())

kk_list = []

for a in range(1, 10):
    for b in range(1, 10):
        kk_list.append(a * b)

if N in kk_list:
    print("Yes")
else:
    print("No")
