N = int(input())
S = input()
print(''.join([chr((ord(s) - ord('A') + N) % 26 + ord('A')) for s in S]))
