t = int(input())
while t>0:
	n, m, h = (float(i) for i in input().split())
	walls = 2 * h * (n + m)
	buckets = walls//16 if walls%16==0 else walls//16+1
	print(int(buckets))

	t -= 1
