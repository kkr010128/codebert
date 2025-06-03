word = input()

num = int(input())
for index in range(num):
    
    code = input().split()
    instruction = code[0]
    start, end  = int(code[1]), int(code[2])

    if instruction == "replace":
        word = word[:start] + code[3] + word[end+1:]
    elif instruction == "reverse":
        reversed_ch = "".join(reversed(word[start:end+1]))
        word = word[:start] + reversed_ch + word[end+1:]
    else:
        print(word[start:end+1])
