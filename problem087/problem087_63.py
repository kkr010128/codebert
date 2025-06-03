#####
# B #
#####

N = input()
sum = sum(map(int,N))

if sum % 9 == 0:
    print('Yes')
else:
    print('No')
