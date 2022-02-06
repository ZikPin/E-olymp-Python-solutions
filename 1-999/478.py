n, m, h = (int(i) for i in input().split())

print(n*m*h, n*m*h*6 - 2*(n*m + m*h + h*n))
