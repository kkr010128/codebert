# Transformation

string = input()
commandAmount = int(input())

for i in range(commandAmount):
    command = input().rstrip().split()
    start = int(command[1])
    end = int(command[2])
    if command[0] == 'print':
        print(string[start : end + 1]) # ここはコメントアウトしないこと
    elif command[0] == 'reverse':
        replacedString = list(string)
        # print(replacedString)
        for i in range(start, end + 1):
            replacedString[i] = list(string)[start + end - i]
        # print(replacedString)
        string = ''.join(replacedString)
    elif command[0] == 'replace':
        string = list(string)
        replace = list(command[3])
        for i in range(start, end + 1):
            string[i] = replace[i - start]
        string = ''.join(string)

