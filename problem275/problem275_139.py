X, Y = tuple(map(int, input().split()))

# Calculate prize for "Coding Contest"
prize_code = 0;
if X == 1:
    prize_code = 300000;
elif X == 2:
    prize_code = 200000;
elif X == 3:
    prize_code = 100000;

# Calculate prize for "Robot Maneuver"
prize_device = 0;
if Y == 1:
    prize_device = 300000;
elif Y == 2:
    prize_device = 200000;
elif Y == 3:
    prize_device = 100000;

# Calculate prize for "two victories"
prize_both = 0
if X == 1 and Y == 1:
    prize_both = 400000

# Calculate the sum and print the answer
prize_total = prize_code + prize_device + prize_both
print(prize_total)