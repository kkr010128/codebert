# // Input
# // 文字列が1行に与えられます。
# // Output
# // 与えられた文字列の小文字と大文字を入れ替えた文字列を出力して下さい。アルファベット以外の文字はそのまま出力して下さい。

line = 'fAIR, LATER, OCCASIONALLY CLOUDY.'
line = input()
output = ''
for i in range(len(line)):
    if line[i].isupper():
        output += line[i].lower()
    elif line[i].islower():
        output += line[i].upper()
    else:
        output += line[i]
print(output)
