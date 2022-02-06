h, w, l, k = tuple([float(i) for i in input().split()])

volume = h * w * l
if volume % k == 0:
  batterys = int(volume/k)
else:
  batterys = int(volume/k) + 1

print(batterys)
