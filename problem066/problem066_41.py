while True:
    h = input()
    h_list = list(h)
    
    if h == '-':
        break
    count = int(input())
    for j in range(count):
        count1 = int(input())
        for i in range(0,count1):
            h_list.append(h_list[0])
            h_list.remove(h_list[0])
            
            length = int(len(h_list))
    for i in range(length):
        print("{}".format(h_list[i]),end="")
    print("")
