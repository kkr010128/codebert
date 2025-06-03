N = input()

l = len(N)

# print(N[l-1])

k = N[l-1]

if k == '2' or k == '4' or k == '5' or k == '7' or k == '9':
    print('hon')
elif k == '0' or k == '1' or k == '6' or k == '8':
    print('pon')
elif k == '3':
    print('bon')