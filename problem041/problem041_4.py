in_str = input().split(" ")
in_width = int(in_str[0])
in_hight = int(in_str[1])

in_x = int(in_str[2])
in_y = int(in_str[3])
in_r = int(in_str[4])

#x check
if (0 <= in_x - in_r) & (in_x + in_r <= in_width):
    #y check
    if (0 <= in_y - in_r) & (in_y + in_r <= in_hight):
        print("Yes")
    else:
        print("No")
else:
    print("No")