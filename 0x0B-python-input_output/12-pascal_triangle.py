#!/usr/bin/python3
'''
pascal triangle solution
'''
def pascal_triangle(n):
  '''
  solve tiangle
  '''
  trangle_list = []
  
  for i in range(n):
    if n <= 0:
      return []
    
    temp = []
    if i == 0:
      temp.append(1)
      triangle_list.append(temp)
      continue
    if i == 1:
      temp.append(1)
      temp.append(1)
      triangle_list.append(temp)
      continue
    
    else:
      j = i - 1
      temp.append(1)
      cur = 0
      nex = 1
      while nex < len(triangle_list[j]):
        s = triangle_list[j][curr] + triangle_list[j][nex]
        temp.append(s)
        curr += 1
        nex += 1
      temp.append(1)
      triangle_list.append(temp)
  return triangle_list    
