n = int(input())
s = input()

[print(chr((ord(s[i])+n-65)%26+65),end="") for i in range(len(s))]
