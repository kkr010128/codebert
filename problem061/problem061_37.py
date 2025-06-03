import re
stt = ""
line = input()
for i in range(len(line)):
    if re.compile("[A-Z]").search(line[i]):
        stt += line[i].lower()
    elif re.compile("[a-z]").search(line[i]):
        stt += line[i].upper()
    else:
        stt += line[i]
print(stt)