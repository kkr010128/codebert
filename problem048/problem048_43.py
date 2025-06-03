cnt = int(input())
values = input()
i_list = [int(x) for x in values.split()]
print('{0} {1} {2}'.format(min(i_list), max(i_list), sum(i_list)))