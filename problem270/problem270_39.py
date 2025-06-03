s = input()

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
ans_dic = {k: v for k, v in zip(week, range(7, 0, -1))}

print(ans_dic[s])
