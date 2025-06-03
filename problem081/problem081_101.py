data = input()
data = data.split()
print("Yes") if int(data[0]) / int(data[2]) <= int(data[1]) else print("No")