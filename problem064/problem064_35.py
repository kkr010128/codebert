str_list = input().rstrip()
str_search = input().rstrip()

str_list = str_list + str_list

if str_search in str_list:
    print("Yes")
else:
    print("No")