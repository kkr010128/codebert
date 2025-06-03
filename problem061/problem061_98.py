import string

s = input()

print(s.translate(str.maketrans(string.ascii_uppercase+string.ascii_lowercase, string.ascii_lowercase+string.ascii_uppercase)))