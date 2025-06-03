S = input()

if(len(S) % 2 != 0):
    print("No")
    exit(0)

for i in range(0, len(S), 2):
    if S[i:i+2] != "hi":
       print("No")
       exit(0)

print("Yes")
