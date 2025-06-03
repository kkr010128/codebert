line = list(map(int,input().split()))
print(line[0]//line[1],line[0]%line[1],'%0.05f'%(1.0*line[0]/line[1]))