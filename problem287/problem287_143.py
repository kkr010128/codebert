N = int(input())

jage = "No"
for l in range(1, 10):
    for r in range(1,10):
        if N == r * l:
            jage = "Yes"
print(jage)