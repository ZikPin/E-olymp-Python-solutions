m = int(input())

def fib(n):
  a, b, c = 2, 4, 7
  if n==1: return a
  elif n==2: return b
  elif n==3: return c
  else:
    for i in range(n-3):
      a, b, c = b, c, a+b+c
    return c
print(fib(m)%12345)
