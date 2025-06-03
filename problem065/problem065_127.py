search = raw_input().upper()
sentence = []
while 1:
    input_data = raw_input()
    if input_data == 'END_OF_TEXT':
        break   
    sentence += [s.upper() for s in input_data.split()]

ret = 0
for word in sentence:
    ret += 1 if word == search else 0
print ret