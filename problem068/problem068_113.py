word = input()
q = int(input())

for _ in range(q):
    s = input().split(" ")
    command = s[0]
    a = int(s[1])
    b = int(s[2])
    if command == "print":
        print(word[a:b+1])
    elif command == "reverse":
        word = word[:a] + word[a:b+1][::-1] + word[b+1:]
    elif command == "replace":
        word = word[:a] + s[3] + word[b+1:]