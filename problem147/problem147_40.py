S = input()
T = input()

if len(S)+1 != len(T):
    print("No")

elif T[0:len(S)] == S:
    print("Yes")

else:
    print("No")