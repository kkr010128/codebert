import sys

read = sys.stdin.read
readline = sys.stdin.readline

n = int(readline())
#print(n)
a_list = list([int(x) for x in readline().rstrip().split()])
#print(a_list)
count = 0
for i in a_list[::2]:
    #print(i)
    if i % 2 != 0:
        count += 1

print(count)
