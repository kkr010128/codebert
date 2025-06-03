def some():
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = int(input())
    s = input()
    result = ""
    for ch in s:
        index = (n + alphabets.index(ch))%26
        result += alphabets[index]
    return result

print(some())