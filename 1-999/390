s = list(input())
n = len(s)
def fak(n):
  if n == 1 or n == 0:
    return 1
  return n*fak(n-1)
f = fak(n)
s.sort()
k = 1
for i in range(0, n-1):
  if s[i] == s[i+1]:
    k += 1
  else:
    f=f//fak(k)
    k=1

print(f//fak(k))
