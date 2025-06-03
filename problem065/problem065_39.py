str_search = input().upper()
int_cnt = 0
len_search = len(str_search)
while True:
    str_line = input()

    if str_line == "END_OF_TEXT":
        break
    
    str_line = str_line.upper()
    int_cnt = int_cnt + str_line.split().count(str_search)

print(str(int_cnt))