a, b = map(int, input().split())
c = str(a)*b
d = str(b)*a
my_list = [c, d]
my_list.sort()
print(my_list[0])