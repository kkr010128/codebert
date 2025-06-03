n = input()
multiplication_table_List = []
for i in range(1,10):
    for j in range(1,10):
        multiplication_table_List.append(str(i*j))
if n in multiplication_table_List:
    print('Yes')
else:
    print('No')