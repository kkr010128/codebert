a = str(input())
b = str(input())
if a[:len(a)] == b[:len(a)] and len(b)==len(a)+1:
    print("Yes")
else:
    print("No")