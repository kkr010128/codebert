n = int(input())
first_list = ['AC', 'WA', 'TLE', 'RE']
list = []
for _ in range(n):
    list.append(input())

for i in first_list:
    print(i, 'x', list.count(i))