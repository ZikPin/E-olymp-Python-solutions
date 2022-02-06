m = int(input())

def fib(n, memo={}):
  if n in memo.keys():
    return memo[n]
  elif n == 1:
    return 2
  elif n == 2:
    return 4

  memo[n] = fib(n-1) + fib(n-2)
  return memo[n]

print(fib(m))
