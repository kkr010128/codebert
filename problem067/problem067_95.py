def main(listseq):
    x = y = 0
    for strings in listseq:
        a, b = strings.split(" ")
        if a < b: y += 3
        elif a > b: x += 3
        elif a == b: x += 1; y += 1
    return x, y


times = int(input())
words = [input() for _ in range(times)]
a, b = main(words)
print(f"{a} {b}")
