S = input()
a = S[0] == 'S'
b = S[1] == 'S'
c = S[2] == 'S'
if (a and b and c ):
    print(0)
elif ( b or(a and c)):
    print(1)
elif(a or c):
    print(2)
else:
    print(3)