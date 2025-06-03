N = int(input())
S = input()
T = ''
for i in S:
    if (ord(i)-64+N)%26 != 0:
        T += chr((ord(i)-64+N)%26 + 64)
    else:
        T += 'Z'
print(T)