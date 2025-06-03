dates = [list(map(int, input().split())) for _ in range(2)]
print("{}".format("1" if dates[0][0] < dates[1][0] or (dates[0][0] == 12 and dates[0][1] == 1) else "0"))