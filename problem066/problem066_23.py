result = []
while True:
    line = input()
    if line is "-":
        break
    count = int(input())
    for _ in range(count):
        n = int(input())
        line = line[n:] + line[:n]
    result.append(line)

print("\n".join(result))
