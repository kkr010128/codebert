input_line1 = raw_input()
work = input_line1.split(' ')

ret = 'a == b'
if int(work[0]) < int(work[1]):
    ret = 'a < b'
if int(work[0]) > int(work[1]):
    ret = 'a > b'
print(ret)