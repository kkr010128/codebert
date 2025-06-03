s= input();
q = int(input());
flag = 0;
fornt = "";
back = "";
while(q>0):
    q-=1;
    ls = list(map(str,input().split(" ")));
    if(ls[0]=='1'):
        flag +=1;
    else:
        if(flag%2 == 1):
            if(ls[1]=='2'):
                fornt=ls[2]+fornt;
            else:
                back=back+ls[2];
        else:
            
            if(ls[1]=='1'):
                fornt=ls[2]+fornt;
            else:
                back=back+ls[2];
s = fornt+s+back
if(flag%2==0):
    print(s);
else:
    print(s[::-1])