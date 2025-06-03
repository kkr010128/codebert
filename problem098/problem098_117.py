N = int(input())
line = input()

R_ = line.count("R")
W_ = line.count("W")

final_line = "R" * R_ + "W" * W_

dic = {"W":0, "R":0}

for idx, c in enumerate(line):
    if c != final_line[idx]:
        dic[c] += 1
        
print(max(dic.values()))