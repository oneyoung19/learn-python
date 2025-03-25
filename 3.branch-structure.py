"""
分支结构
if __name__ == '__main__':
else:

if :
elif :
else :

match :
  case :
  case :
  case _:
"""

value = int(input('请输入一个数字: '))
1
if 1 <= value <= 100:
  print('数字在1到100之间')
elif 100 < value <= 1000:
  print('数字在100到1000之间')
else:
  print('数字不在1到1000之间')

# python@3.10才支持
# match value:
#   case 1:
#     print('数字是1')
#   case 2:
#     print('数字是2')
#   case _:
#     print('数字不是1也不是2')