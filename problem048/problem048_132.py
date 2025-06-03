n = input()

min_num = 1000001
max_num = -1000001
sum = 0

tmp = map(int, raw_input().split())
for i in xrange(n):
    min_num = min(min_num, tmp[i])
    max_num = max(max_num, tmp[i])
    sum += tmp[i]
    
print "%d %d %d" % (min_num, max_num, sum)