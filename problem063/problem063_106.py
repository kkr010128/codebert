import string
import sys
text = sys.stdin.read().lower()
for char in string.ascii_lowercase:
    print(char, ':', text.count(char))

