price_list = []
t = raw_input()
for i in range(int(t)):
    price_list.append(int(input()))
maxv = float("-inf")
minv = price_list[0]
for i in range(1, int(t)):
    maxv = max([maxv, price_list[i] - minv])
    minv = min([minv, price_list[i]])
print maxv