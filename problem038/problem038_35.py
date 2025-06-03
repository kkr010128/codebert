num = input()
num_list = []
num_list = num.split()

if int(num_list[0]) == int(num_list[1]):
    print('a','b',sep=' == ')
elif int(num_list[0]) > int(num_list[1]):
    print('a','b',sep=' > ')
else:
    print('a','b',sep=' < ')