c = input()
alphabet = [chr(i) for i in range(97, 97+26)]

idx = alphabet.index(c)
print(alphabet[idx+1])
