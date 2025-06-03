n = int(input())

num_list = [int(i) for i in input().split(" ")]

a = min(num_list)
b = max(num_list)
c = sum(num_list)

print("{0} {1} {2}".format(a, b, c))