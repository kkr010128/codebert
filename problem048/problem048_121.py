raw_input()
num_list = map(int, raw_input().split(" "))
print "%d %d %d" % (min(num_list), max(num_list), sum(num_list))