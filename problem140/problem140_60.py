t=input()
result=''
for i in range(len(t)-1):
    if t[i]=='?':
        try:
            if result[i-1]=='P':
                result+='D'
            else:
                if t[i+1]=='P':
                    result+='D'
                else:
                    result+='P'
        except:
            if t[i+1]=='P':
                result+='D'
            else:
                result+='P'
    else:
        result+=t[i]
if t[len(t)-1]=='?' or  t[len(t)-1]=='D':
    print(result+'D')
else:
    print(result+'P')