N = list(input())
l = len(N)
if N[l-1] == '2' or N[l-1] == '4' or N[l-1] == '5' or N[l-1] == '7' or N[l-1] == '9':
    print('hon')
elif N[l-1] == '0' or N[l-1] == '1' or N[l-1] == '6' or N[l-1] == '8':
    print('pon')
elif N[l-1] == '3':
    print('bon')