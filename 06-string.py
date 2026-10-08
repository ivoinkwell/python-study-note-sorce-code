# formatted output

'''

formatted output demo

'''

# printf-stylr formatting

name = 'ivoinkwell'
age = 17
print("姓名是：%s, 年龄是：%d" % (name, age))

# str.fromatting

print("姓名是：{}, 年龄是：{}".format(name, age))

print("姓名是：{1}, 年龄是：{0}".format(age, name))

print("姓名是：{name}, 年龄是：{age}".format(name=name, age=age))

print("姓名是：{name}, 年龄是：{age}".format(age=age, name=name))

# f-string

print(f"姓名是：{name}, 年龄是：{age}")