X = int(input())

facts = [0]
n = 1
while True:
    facts.append(n ** 5)
    if facts[-1] - facts[-2] > X:
        break
    n += 1

facts = set(facts)

for f0 in facts:
    f1 = None
    if abs(f0 - X) in facts:
        f1 = abs(f0 - X)
        r0 = int(f0 ** 0.2)
        r1 = int(f1 ** 0.2)
        if f0 - f1 == X:
            print(r0, r1)
        else:
            print(r0, -r1)
        break
