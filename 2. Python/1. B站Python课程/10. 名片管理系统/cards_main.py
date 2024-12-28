import cards_tools as ct  # 导入工具包


card_list = []

while True:     # 主循环
    ct.print_title()
    
    slt = input("请输入要进行的操作：")
    print("*" * 50)

    if slt == "0":  
        # 输入0退出
        break

    elif slt == "1":
        # 新建名片
        card_list.append(ct.create_card())

    elif slt == "2":
        # 显示全部
        ct.show_card(card_list)

    elif slt == "3":
        # 查询和修改名片
        card_list = ct.modify_card(card_list) # 该函数会返回值
        print(card_list)
        print(type(card_list))
