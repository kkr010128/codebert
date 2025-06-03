a = [input() for i in range(2)]
b = a[1].split(" ")
ans = 0

num = int(a[0])
if num>2:
  for i in range (0,num-2):
    for j in range (i+1,num-1):
      for k in range (j+1, num):
        if int(b[i])!=int(b[j]):
          if int(b[j])!=int(b[k]):
            if int(b[k])!=int(b[i]):
              if int(b[i])+int(b[j])>int(b[k]):
                if int(b[j])+int(b[k])>int(b[i]):
                  if int(b[k])+int(b[i])>int(b[j]):
                    ans=ans+1
print(ans)