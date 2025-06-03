list = []
n = int(raw_input())
list = map(int, raw_input().split(' '))
list.reverse()
for i in range(len(list)):
    print list[i],