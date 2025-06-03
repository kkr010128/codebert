s = input()
T = input()

if T[:len(T)-1] == s and len(s)+1 == len(T):
    print("Yes")
else:
    print("No")