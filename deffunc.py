#定义一个求幂函数
'''
def power(x, n):
    s = 1
    while n > 0:
        s = s*x
        n = n-1
    return s

print(power(5,2))
'''

'''
def calc(nums):
    s = 0
    for i in nums:
        s = s + i*i
    return s
nums1 = [1,3,5]
print(calc(nums1))
'''
#这是可变参数 传入的是 list 或 tuple
'''
def calc(*nums):
    s = 0
    for i in nums:
        s = s + i*i
    return s
print(calc(1,2,3))
num1 = [1,2,3]
print(calc(*num1))
'''
#关键字参数和命名关键字参数 传入的是一个dict
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def concact(name, age, **kw):
    if 'high' in kw:
        print("high")
    print("name=", name, "age", age, "others", kw)
concact("zhangsan", 15,  high=178, weight=82)

body = {'high': 178, 'weight': 83}
concact("lisi", 35, **body)
'''
