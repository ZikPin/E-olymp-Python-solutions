x1, y1, r1, x2, y2, r2 = (float(i) for i in input().split()) # get the variables

biggest_r = max(r1, r2)
smallest_r = min(r1, r2)

distance = ( (x1-x2)**2 + (y1-y2)**2 )**(1/2) # finding distance between center points of circle

if x1 == x2 and y1 == y2 and r1 == r2: # if they have same coordinates and radiuses
  print(-1)
elif distance == r1 + r2: # if they touch each other from outside
  print(1)
elif distance > r1 + r2: # if they are too far from each other
  print(0)
elif distance < r1 + r2: # if one circle is inside other
  if distance < biggest_r and distance + smallest_r < biggest_r: 
    print(0)
  elif distance < biggest_r and distance + smallest_r == biggest_r:
    print(1)
  else:
    print(2)
