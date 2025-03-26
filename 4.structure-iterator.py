"""
1. for in

2. while

"""
import time

for _ in range(3):
  print('range')
  time.sleep(1)

for index in [1, 2, 3]:
  print('list', index)
  time.sleep(1)

for index, value in enumerate([1, 2, 3]):
  print('enumerate', index, value)
  time.sleep(1)