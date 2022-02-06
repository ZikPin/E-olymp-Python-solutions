t1, t2, t3 = tuple([float(i) for i in input().split()])

ans = 0.00
if t1 != 0 and t2 != 0 and t3 != 0:
  ans=1/(1/t1 + 1/t2 + 1/t3)
  ans=round(ans, 2)
  ans += 0.0001

print(str(ans)[:-2])
