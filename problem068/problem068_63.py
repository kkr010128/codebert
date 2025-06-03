import sys

input = sys.stdin.readline

def main():
    text = input().rstrip()
    n = int(input().rstrip())
    for i in range(n):
        s = input().split()
        if s[0] == "print":
            print(text[int(s[1]):int(s[2])+1])
        elif s[0] == "replace":
            new_text = ""
            new_text += text[:int(s[1])]
            new_text += s[3]
            new_text += text[int(s[2])+1:]
            text = new_text
        elif s[0] == "reverse":
            new_text = ""
            new_text += text[:int(s[1])]
            for i in range(int(s[2])-int(s[1]) + 1):
                new_text += text[int(s[2]) - i]
            new_text += text[int(s[2])+1:]
            text = new_text
        
if __name__ == "__main__":
    main()
