while True :
    str = input()
    if str == '-' : exit()
    times = int(input())
    for i in range(times) :
       h = int(input())
       s_f = str[:h]
       s_l = str[h:]
       str = s_l + s_f
    print(str)