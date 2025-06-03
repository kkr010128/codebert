N = int(input())
target_list = []
if N % 2 == 1:
    N += 1
for i in range(1, int(N/2)):
    target = N - i
    if target == i:
        continue
    else:
        target_list.append(target)

print(len(target_list))