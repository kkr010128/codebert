import sys
#入力する名前S
S = input()

#新しいID T
T = input()

#print(S)
#print(type(S))
#print(T)
#print(type(T))

if S == T[:-1]:
    print("Yes")
    sys.exit()

else:
    print("No")