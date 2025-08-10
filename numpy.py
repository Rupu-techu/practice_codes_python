import numpy as np

rows = int(input('rows: '))
cols = int(input('cols: '))

print('enter the elements of the 1st array (one row at a time): ')
l1 = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    l1.append(row)

print('enter the elements of the 2nd array (one row at a time): ')
l2 = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    l2.append(row)

a1 = np.array(l1)
a2 = np.array(l2)

add = a1 + a2
mul = np.matmul(a1,a2)

print('result:')
print(add)
print(mul)