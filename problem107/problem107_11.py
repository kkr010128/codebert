n = int(input())
x = input()

init_pop_cnt = x.count('1')
init_pop_cnt_less = init_pop_cnt - 1
init_pop_cnt_more = init_pop_cnt + 1

valid_l = init_pop_cnt_less != 0

# x's state after f
init_res_less = 0
init_res_more = 0
seed_more = 1
seed_less = 1
for i in range(1, n+1):
  xp = x[-1 * i]
  if xp == '1':
    if valid_l:
      init_res_less += seed_less % init_pop_cnt_less
    init_res_more += seed_more % init_pop_cnt_more
  if valid_l:
    seed_less = (seed_less * 2) % init_pop_cnt_less
  seed_more = (seed_more * 2) % init_pop_cnt_more


dif_less = [0] * (2 * 10**5 + 100)
dif_more = [0] * (2 * 10**5 + 100)
if valid_l:
  dif_less[0] = 1 % init_pop_cnt_less
dif_more[0] = 1 % init_pop_cnt_more
for i in range(1, n+1):
  if valid_l:
    dif_less[i] = (dif_less[i-1] * 2) % init_pop_cnt_less
  dif_more[i] = (dif_more[i-1] * 2) % init_pop_cnt_more


def get_pc(dec):
  out = 0
  while dec > 0:
    if dec % 2 == 1:
      out+=1
    dec = dec // 2
  return out

def f(dec):
  pc = get_pc(dec)
  return dec % pc

cnt = [0] * (2 * 10**5 + 200)

for i in range(1, 2 * 10**5 + 100):
  c = 0
  cur = i
  while cur > 0:
    c += 1
    cur = f(cur)
  cnt[i] = c

for i in range(n):
  xi = x[i]

  if xi == '1':
    if valid_l:
      lx = init_res_less
      lx -= dif_less[n-i-1]
      lx %= init_pop_cnt_less
      print((cnt[lx] % init_pop_cnt_less) + 1)
    else:
      print(0)
  else:
    lx = init_res_more
    lx += dif_more[n-i-1]
    lx %= init_pop_cnt_more
    print((cnt[lx] % init_pop_cnt_more) + 1)
