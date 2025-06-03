import sys
count = [0 for _ in range(ord("a"), ord("z") + 1)]
for line in sys.stdin:
    for c in list(line.lower()):
        if "a" <= c <= "z":
            count[ord(c) - ord("a")] += 1
for i, n in enumerate(count):
    print("{ch} : {cnt}".format(ch = chr(ord("a") + i), cnt = n))


