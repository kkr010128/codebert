import re
s = input()
bl = re.fullmatch(r"^(hi)+$", s) is not None
print("Yes" if bl else "No")