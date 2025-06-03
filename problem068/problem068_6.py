s = input()
q = int(input())
for _ in range(q):
    line = input().split()
    if line[0] == 'print':
        print(s[int(line[1]):int(line[2]) + 1])
    elif line[0] == 'reverse':
        s1 = s[:int(line[1])]
        s2 = s[int(line[1]):int(line[2]) + 1]
        s2 = s2[::-1]
        s3 = s[int(line[2]) + 1::]
        s = s1 + s2 + s3
    elif line[0] == 'replace':
        s1 = s[:int(line[1])]
        s2 = s[int(line[2]) + 1:]
        s = s1 + line[3] + s2
