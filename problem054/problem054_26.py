all_set = ['S ' + str(i) for i in range(1, 14)] + ['H ' + str(i) for i in range(1, 14)] + ['C ' + str(i) for i in range(1, 14)] + ['D ' + str(i) for i in range(1, 14)]
r = int(input())

for _ in range(r):
    x = input()
    if x in all_set:
        del all_set[all_set.index(x)]
        
for i in all_set:
    print(i)
