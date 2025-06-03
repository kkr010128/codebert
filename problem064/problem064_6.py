s = input()
p = input()
ret = 'No'
tts = s + s[:len(p)]
if p in tts: ret = 'Yes'
print(ret)
