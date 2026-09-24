# 会员评定系统

M = float(input("请输入消费金额"))
S = float(input("请输入积分"))

if S < 500:
    print("普通会员")
elif 500 < S < 1000:
    print("青铜会员")
elif 100 <= M < 200 and 1000 <= S < 2000:
    print("白银会员")
elif 200 <= M < 500 and 2000 <= S < 5000:
    print("黄金会员")
elif 500 <= M < 1000 and 5000 <= S < 10000:
    print("白金会员")
elif M >= 1000 and S >= 10000:
    print("钻石会员")

# 物流费用计算

address = input("请输入地区编号：")
weight = int(input("请输入寄件重量(kg)："))

def number1(weight):
    add_weight = float(float(weight)*3)

    if weight <= 2:
        return 13
    else:
        return 13 + add_weight

def number2(weight):
    add_weight = float(float(weight)*2)

    if weight <= 2:
        return 12
    else:
        return 12 + add_weight

def number3(weight):
    add_weight = float(float(weight)*4)

    if weight <= 2:
        return 14
    else:
        return 14 + add_weight

if __name__ == "__main__":
    if address == "01":
        print("价格是：", number1(weight), "元")
    elif address == "02":
        print("价格是：", number2(weight), "元")
    else:
        print("价格是：", number3(weight), "元")