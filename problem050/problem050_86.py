while 1:
 w,h=map(int,raw_input().split())
 if(w==0):break
 a,b="#\n";print a*h+b+(a+"."*(h-2)+a+b)*(w-2)+a*h+b