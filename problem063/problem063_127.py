data = ""
data_1 = [chr(ord('a') + i) for i in range(26)]
while True:
    try:
        data += input().lower()
    except EOFError:
        break
for i in data_1:
    j = data.count(i)
    print(f'{i} : {j}')
