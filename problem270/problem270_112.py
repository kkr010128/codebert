S = input()
wait_day = 0

if S == "SUN":
  wait_day = 7
elif S == "MON":
  wait_day = 6
elif S == "TUE":
  wait_day = 5
elif S == "WED":
  wait_day = 4
elif S == "THU":
  wait_day = 3
elif S == "FRI":
  wait_day = 2
elif S == "SAT":
  wait_day = 1

print(wait_day)