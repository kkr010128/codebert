s = input()
left_index = []
puddles = []

for i in range(len(s)):
    if s[i] == "\\":
        left_index.append(i)

    elif s[i] == "/" and len(left_index) > 0:
        left = left_index.pop()
        puddle = i - left

        while len(puddles) > 0 and puddles[-1][0] > left:
            puddle += puddles.pop()[1]

        puddles.append([left, puddle])

ans = [p[1] for p in puddles]
print(sum(ans))
if len(ans): print(len(ans), " ".join(map(str, ans)))
else : print(len(ans))

