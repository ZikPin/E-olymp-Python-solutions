n = int(input())
i = 1
counter = 0
while i <= n:
	if n%i == n//i:
		counter += 1
	i += 1
print(counter)
