def flowers(n):
	arrangement = ["VGC", "CVG", "GCV"]
	return arrangement[n%3-1]

t = int(input())
while t > 0:
	n = int(input())
	print(flowers(n))
	t -= 1
