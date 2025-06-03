n = int(input())
j_list = [input() for x in range(n)]

print("AC x",j_list.count("AC"))
print("WA x",j_list.count("WA"))
print("TLE x",j_list.count("TLE"))
print("RE x",j_list.count("RE"))