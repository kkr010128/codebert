C = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[(alphabet.index(C) + 1) % len(alphabet)])