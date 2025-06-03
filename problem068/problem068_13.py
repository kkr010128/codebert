string = input()
n = int(input())
print_s=[]
for i in range(n):
    order = [i for i in input().split()]
    if order[0] == "replace":
        string = list(string)
        for i in range(len(order[3])):
            string[int(order[1])+i]=order[3][i]
        string= "".join(string)
    elif order[0] == "reverse":
        string = string.replace(string[int(order[1]):int(order[2])+1],
                                string[int(order[2])-len(string):
                                       int(order[1])-len(string)-1:-1])
    else:
        print_s.append(string[int(order[1]):int(order[2])+1])
for i in range(len(print_s)):
    print(print_s[i])
