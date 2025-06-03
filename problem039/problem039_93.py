in_str = input()
temp_list = in_str.split()
a = int(temp_list[0])
b = int(temp_list[1])
c = int(temp_list[2])
if abs(a) <= 100 and abs(b) <= 100 and abs(c) <= 100:
    print("Yes" if a < b < c else "No")