#first

s1 = set(['key1', 'key2', 'key3', 'key1'])
s2 = set(['key2', 'key3', 'key4'])

s3 = s1 & s2
s4 = s1 | s2

s4.add(1)
s4.remove('key2')
print(s1)
print(s2)
print(s3)
print(s4)











