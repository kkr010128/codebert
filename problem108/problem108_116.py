Nin = int(input())

noguchi = (Nin // 1000)
if (Nin % 1000):
    noguchi += 1

print(noguchi*1000 - Nin)
