N = int(input())
multiple_list = {i*j for i in range(1,10) for j in range(1,10)}
print(['No','Yes'][N in multiple_list])