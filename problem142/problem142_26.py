import re

n = input()

if len(re.findall("2|4|5|7|9", n[-1])) > 0:
    print("hon")
elif len(re.findall("0|1|6|8", n[-1])) > 0:
    print("pon")
else:
    print("bon")
