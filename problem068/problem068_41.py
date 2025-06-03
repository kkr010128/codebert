word = input()
n = int(input())
for _ in range(n):
    meirei = input().split()
    if meirei[0] == "print":
        print(word[int(meirei[1]):int(meirei[2])+1])
    elif meirei[0] == "reverse":
        word = word[:int(meirei[1])] + word[int(meirei[1]):int(meirei[2])+1][::-1] + word[int(meirei[2])+1:]
    elif meirei[0] == "replace":
        word = word[:int(meirei[1])] + meirei[3] + word[int(meirei[2])+1:]
        
