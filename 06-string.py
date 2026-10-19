# formatted output

'''

formatted output demo

'''

# printf-style formatting

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

# .islower()

s = 'AbcDeFGhIJ'
count = 0
for ch in s:
    if ch.islower():   # 字符串方法：判断是否小写字母
        count += 1
print(count)

# .replace()

s = "Life is short. I use python"
if "python" in s:              # in：检查子串是否存在
    s = s.replace("python", "Python")  # 字符串方法：替换子串
print(s)

# 水仙花数

number = input("请输入一个数字: ")

total = 0

for i in number:
    total += int(i)**3

if total != int(number):
    print(f"{number}不是水仙花数")
else:
    print(f"{number}是水仙花数")