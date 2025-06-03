n = int(input())

count_list = [0] * 4

for i in range(n):
    text = input()
    if text == "AC":
        count_list[0] += 1
    elif text == "WA":
        count_list[1] += 1
    elif text == "RE":
        count_list[3] += 1
    else:
        count_list[2] += 1

print("AC x " + str(count_list[0]))
print("WA x " + str(count_list[1]))
print("TLE x " + str(count_list[2]))
print("RE x " + str(count_list[3]))