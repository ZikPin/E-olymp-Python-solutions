import math

n = int(input())
counter = 0

while n > 1:
	log_of_n = math.log2(n)
	if log_of_n - int(log_of_n) == 0:
		counter += log_of_n
		break
	elif n%2 == 0:
		counter += 1
		n //= 2
	else:
		counter += 1
		n += 1
	
print(int(counter))
