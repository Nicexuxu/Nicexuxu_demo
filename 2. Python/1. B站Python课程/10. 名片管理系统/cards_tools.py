def print_title():
    # 打印欢迎界面
    print("\n" * 5)
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询及修改名片")
    print()
    print("0. 退出系统")
    print("*" * 50)




def create_card():
    # 添加名片
    dict_add = {}
    dict_add["name"] = input("请输入姓名")
    dict_add["phone"] = input("请输入电话")
    dict_add["qq"] = input("请输入QQ号码")
    dict_add["email"] = input("请输入邮箱")
    input("输入成功，按enter回到主界面")
    return dict_add




def show_card(card_list):
    
    if len(card_list) == 0:
        print("当前暂无名片")
    else:
        for i in card_list:
            print("姓名:", i["name"], end="\t")
            print("电话:", i["phone"], end="\t")
            print("QQ:", i["qq"], end="\t")
            print("邮箱:", i["email"])

    input("按enter回到主界面")




def modify_card(card_list):
    # 该函数需要返回值

    while True:
        ctn = 1    # 用于待会判断要不要退出循环

        find = input("请输入要查找的姓名：")
        for i in card_list:
            if i["name"] == find:       # if引导的都是找到名片后的内容
                print("成功找到名片：")
                print("姓名:", i["name"], end="\t")
                print("电话:", i["phone"], end="\t")
                print("QQ:", i["qq"], end="\t")
                print("邮箱:", i["email"])
                slt = input("请输入输入要进行的操作：1修改，2删除，3返回主菜单")           


                if slt == "1":
                    mdf = i
                    a = input("请输入修改后的姓名(按enter不修改)")
                    if a != "":
                        mdf["name"] = a

                    b = input("请输入修改后的电话(按enter不修改)")
                    if b != "":
                        mdf["phone"] = b

                    c = input("请输入修改后的QQ(按enter不修改)")
                    if c != "":
                        mdf["qq"] = c

                    d = input("请输入修改后的邮箱(按enter不修改)")
                    if d != "":
                        mdf["email"] = d

                    card_list[card_list.index(i)] = mdf
                    input("修改成功，按enter回到主菜单")
                    return card_list    # 返回修改后值
                

                if slt == "2":
                    card_list.remove(i)
                    input("删除成功，按enter回到主菜单")
                    return card_list    # 返回删除后值
                

                if slt == "3":
                    return card_list    # 返回没有更改过的值  
            
        

        else:   # else引导没有找到名片后的内容
            panduan = input("未找到该名片，是否重新查找？【Y/n】")
            if panduan in ["N", "n", "No", "no"]:
                ctn = 0
        

        if ctn == 0:    # 判断是否退出循环，并返回值
            return card_list
        



