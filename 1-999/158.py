def fibo(num):
  fib= [1, 1, 1, 1]

  for i in range(4, num+1):
    fib.append(fib[i-1]+fib[i-2]+fib[i-3]+fib[i-4])

  return fib

i = int(input())
nums = []
for k in range(i):
  nums.append(int(input()))

fib = fibo(max(nums))
[print(fib[i-1]) for i in nums]
