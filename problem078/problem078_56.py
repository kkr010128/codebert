input_line = int(input())

if input_line > 1 :
    count = 10**input_line - 8**input_line - (9**input_line - 8**input_line) * 2
    print(count % (10**9 + 7))
else :
    print(0)