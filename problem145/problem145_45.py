

# ABC168D
# https://atcoder.jp/contests/abc168/tasks/abc168_d

n,m=map(int, input().split())
ab=[[]for _ in range(n)]
for i in range(m):
    a,b = list(map(int, input().split()))
    a,b = a-1, b-1
    ab[a].append(b)
    ab[b].append(a)
    '''
    まず両方を追加する考えがなかった。
    浅い部屋からも深い部屋からも参照できる。
    その代わりに visitedで考えなくて良い部屋を記録している。
    部屋１につながっているのはもっとも浅い部屋でそこから考えることがきっかけになる？
    '''
#print(ab)
ans = [0]*n
visited={0}
stack=[0]
for i in stack:
    '''
    現在考えている部屋を stack、そこにつながる部屋 ab[i]として考える。
    stack=[0]なので1の部屋から始める。なので深さ1の部屋が ab[i](ab[0])で分かる。
    i==0の始めの一周では、ab[i]は深さ１の部屋のリストであり、それぞれの部屋を jとして順番に考える。
    (このように深さ1から考えられる＋次に深さ2の部屋を求めるというのが上手くいく)
    その現在考えている部屋 i(stackの循環)とそこにつながる部屋 j(abの循環)なので、
    部屋 jはより浅い部屋 iを道しるべにすればよい。
    しかし、ab[a], ab[b]と両方を追加しているので、浅い部屋も深い部屋も abには含まれている。
    浅い部屋から順に考えているので、過去に調べた abの値は無視するために visitedを導入する。たぶん。
    '''
    for j in ab[i]:
        #print(i,j,'----------------------')
        if j in visited:
            continue
        stack.append(j)
        visited.add(j)
        ans[j]=i+1
        #print('stack', stack)
        #print('visited', visited)
        #print('ans', ans)
check=0
for i in ans[1:]:
    if i==0:check==1
if check:
    print('No')
else:
    print("Yes")
    print(*ans[1:])
