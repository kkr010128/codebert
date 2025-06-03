num_freebies = int(input())

freebies = []

for _ in range(num_freebies):
    freebies.append(input())

print(len(set(freebies)))
