import string

print(input().translate(str.maketrans(
    string.ascii_uppercase + string.ascii_lowercase,
    string.ascii_lowercase + string.ascii_uppercase)))