N = int(input()) 
S = input()

if N%2 == 1:
    print("No")
else:
    print("Yes") if S[:len(S)//2] == S[len(S)//2:] else print("No")