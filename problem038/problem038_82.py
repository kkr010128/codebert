a = input().split()
if -1000 > int(a[0]):
    print('')
elif 1000 < int(a[0]):
    print('')    
elif -1000 > int(a[1]):
    print('')
elif 1000 < int(a[1]):
    print('')    
elif int(a[0]) < int(a[1]):
    print('a < b')
elif int(a[0]) > int(a[1]):
    print('a > b')
elif int(a[0]) == int(a[1]):
    print('a == b')
