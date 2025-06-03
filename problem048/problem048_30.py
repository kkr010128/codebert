raw_input()
list = list(map(int,raw_input().split()))
list.sort()
print list[0],list[len(list) - 1],sum(list)