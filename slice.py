#切片测试
'''
testlist = list(range(100))
print(testlist[-1])
print(testlist[:])
print(testlist[1:33:2])
print(testlist[-2:-1])
print(testlist[-2:])
'''

list1 = [x*x  for x in range(1, 11) if x%2 == 0]
print(list1)