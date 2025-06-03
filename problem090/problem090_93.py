num = input()

streaks = []
streak = 0
for letter in num:
    if letter == "R":
        streak += 1
    elif letter != "R":
        streaks.append(streak)
        streak = 0
else:
    streaks.append(streak)

print(max(streaks))