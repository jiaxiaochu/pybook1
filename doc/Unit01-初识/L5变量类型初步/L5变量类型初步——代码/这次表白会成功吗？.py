import random

a = 0
while a < 1:
    biaobai = random.choice([True, False])
    b = input("要跟女神表白吗？要，输入1，不要输入2")
    if b == "1":
        if biaobai == True:
            print("恭喜你，女神同意了，表白成功！撒花🎉🎉🎉")
            print("此时变量biaobai的值为：" + str(biaobai))
        if biaobai == False:
            print("很遗憾，女神拒绝了，表白失败😭😭😭")
            print("此时变量biaobai的值为：" + str(biaobai))
    elif  b == "2":
        print("有病呀，不来表白还运行个毛的程序，祝孤生！")
    else:
        print("不要紧张，表白没什么的，请按照提示输入😊")