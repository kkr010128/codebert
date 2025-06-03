num_employees = int(input())

bosses = list(map(int, input().split()))

counter = [0] * num_employees

for boss in bosses:
    counter[boss - 1] += 1

print('\n'.join(map(str, counter)))
