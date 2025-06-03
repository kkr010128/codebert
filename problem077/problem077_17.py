a, b, c, d = map(int, input().split())

x_li = [a, b]
y_li = [c, d]

my_list = []

for x in x_li:
    for y in y_li:
        my_list.append(x * y)
        
print(max(my_list))