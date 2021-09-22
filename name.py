while 1:
    score = input("please int your score:")
    score = int(score)
    if   score > 0 and score <= 20:
            print("你的等级是E。")
    elif score > 20 and score <= 40:
            print("你的等级是D。")
    elif score > 40 and score <= 60:
            print("你的等级是C。")
    elif score > 60 and score <= 80:
            print("你的等级是B。")
    elif score > 80 and score <= 100:
            print("你的等级是A。")    
    else:
            print("瞎扯淡")
print("输入结束")


