n, m = map(int, input().split())
submissions = [list(input().split()) for _ in range(m)]
count_penalty = [0] * (n + 1)
count_ac = [0] * (n + 1)

for i in range(m):
    ploblem = int(submissions[i][0])
    if submissions[i][1] == "AC":
        count_ac[ploblem] = 1

    elif count_ac[ploblem] != 1 and submissions[i][1] == "WA":
        count_penalty[ploblem] += 1

for i in range(n + 1):
    if count_ac[i] != 1:
        count_penalty[i] = 0

print("{} {}".format(count_ac.count(1), sum(count_penalty)))
