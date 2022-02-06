h1, m1, s1 = (int(i) for i in input().split())
h2, m2, s2 = (int(i) for i in input().split())

overall1 = h1 * 3600 + m1 * 60 + s1
overall2 = h2 * 3600 + m2 * 60 + s2

result = overall2 - overall1

hour = result // 3600
result = result % 3600
minute = result // 60
result = result % 60
second = result

print(hour, minute, second)
