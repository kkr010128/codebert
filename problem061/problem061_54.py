answer_string=''
string=input()
for i in string:
    if i.isupper():
        i=i.lower()
    elif i.islower():
        i=i.upper()
    answer_string+=i
print(answer_string)
