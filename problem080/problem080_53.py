N = int(input())

#https://img.atcoder.jp/abc178/editorial-E-phcdiydzyqa.pdf

z_list = list()
w_list = list()

for i in range(N):
    x,y = map(int, input().split())
    z_list.append(x + y)
    w_list.append(x - y)
    
print(max(max(z_list)-min(z_list),max(w_list)-min(w_list)))