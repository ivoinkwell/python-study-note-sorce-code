i = 0
j = 0

# While语句
while i < 100:
    print("Hello")
    i += 1

# 输出 1+……+100
while i < 100:
    i += 1
    j += i
print(j)

for i in range(1, 101):
    j += i
print(j)

# for 循环

# 步长
# for a in range(1, 10, -1):
#     print("a = ", a)

for a in range(1, 10):
    print("a = ", a)

for a in range(4):
    print("Hello")

# 斐波那契数列
n = int(input("请输入n: "))

a = 0
b = 1

for i in range(n):
    print(a)

    c = a + b
    a = b
    b = c