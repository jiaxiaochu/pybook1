# 没有类型转换前
# xiaomingAge = input("请输入小明的年龄")
# xiaoqiangAge = input("请输入小强的年龄")
# print("小明和小强的年龄之和为：", xiaomingAge + xiaoqiangAge)
# 出了问题，闹了笑话怎么办呢？
# xiaomingAge = input("请输入小明的年龄")
# xiaoqiangAge = input("请输入小强的年龄")
# print(type(xiaomingAge), type(xiaoqiangAge)) # 检查一下是不是像所说的那样，input的内容都是字符串
# 类型转换之后
xiaomingAge = input("请输入小明的年龄")
xiaoqiangAge = input("请输入小强的年龄")
print("小明和小强的年龄之和为：", int(xiaomingAge) + int(xiaoqiangAge))