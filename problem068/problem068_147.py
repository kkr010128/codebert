string = list(input())
times = int(input())
#a = [int(i) for i in range(0,5)]
#print(a)
for i in range(times):
    order = input().split()
    #print(order)
    if order[0] == "replace":
        replace_string = order[3]
        #print(string)
        count = 0
        for j in range(int(order[1]), int(order[2]) + 1):
            string[j] = replace_string[count]
            count += 1
            #print(count)
        #print(string)
    elif order[0] == "reverse":
        #print(string)
        reverse_string = string[int(order[1]):int(order[2]) + 1]
        reverse_string.reverse()
        #for j in range(int(order[1]), int(order[2]) + 1):
        #    string[j] = reverse_string[j]
        string = string[:int(order[1])] + reverse_string + string[int(order[2])+1:]
        #print(j)
        #print(string)
        #string[int(order[1]):int(order[2]) + 1].reverse()
        #print(string)
        #string[int(order[1]):int(order[2])] = string[int(order[1]):int(order[2])].reverse()
    elif order[0] == "print":
        #print(string)
        print("".join(string[int(order[1]):int(order[2]) + 1]))
        #print(string)