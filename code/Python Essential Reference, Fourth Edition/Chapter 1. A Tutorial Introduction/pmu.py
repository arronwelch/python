import sys
str = sys.stdin.readline()
list = str.split(":")
print(list)

for i in list:
    i = int(i)
    print("%3d" % (i), end = ' ')
    print("%3d" % (i%16), end = ' ')
    print(type(i))
