string = input()
for i in range(int(input())):
    lst = list(map(str, input().split()))
    if lst[0] == "replace":
        string = string[:int(lst[1])] + lst[3] + string[int(lst[2])+1:]
    if lst[0] == "reverse":
        rev_str = str(string[int(lst[1]):int(lst[2])+1])
        string = string[:int(lst[1])] + rev_str[::-1] + string[int(lst[2])+1:]
    if lst[0] == "print":
        print(string[int(lst[1]):int(lst[2])+1])

