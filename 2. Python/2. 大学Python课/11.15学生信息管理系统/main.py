def print_menu():
    print("\n" * 5)
    print("*" * 50)
    print("欢迎使用【学生信息管理系统】v1.0")
    print("")
    print("1. 增加学生信息")
    print("2. 查看所有学生信息")
    print("3. 修改学生信息")
    print("4. 删除学生信息")
    print("")
    print("0. 退出学生信息管理系统")
    print("*" * 50)


def student_add():
    global students_list
    dict_add = {}
    name = input("请输入姓名：")
    for i in students_list:
        if i["name"] == name:
            input("系统已存在该学生信息，请勿重复添加，按Enter回到主菜单")
            break
    else:
        dict_add["name"] = name        
        dict_add["num"] = input("请输入学号：")
        dict_add["age"] = input("请输入年龄：")
        students_list.append(dict_add)
        input("创建成功，按Enter回到主菜单")


def show_students():
    global students_list
    if len(students_list) == 0:
        input("当前暂无学生信息\n按Enter回到主菜单")
    else:
        print("当前存在%s个学生信息：" % len(students_list))
        for i in students_list:
            print("姓名：", i["name"], end="\t\t\t")
            print("学号：", i["num"], end="\t\t\t")
            print("年龄：", i["age"])
        input("按Enter回到主菜单")


def modify_students():
    global students_list
    while True:
        find = input("请输入要修改的学生名称：")
        for i in students_list:
            if i["name"] == find:
                dict_modified = i
                modified = input("请输入修改后的名称：(按Enter不修改)")
                if modified != "":
                    dict_modified["name"] = modified
                modified = input("请输入修改后的学号：(按Enter不修改)")
                if modified != "":
                    dict_modified["num"] = modified
                modified = input("请输入修改后的年龄：(按Enter不修改)")
                if modified != "":
                    dict_modified["age"] = modified
                students_list[students_list.index(i)] = dict_modified
                input("修改成功，按Enter回到主菜单")
                return
        else:
            ctn = input("未找到该学生，是否重新输入并查找？【Y/n】")
            if ctn in ["N", "No", "n", "no"]:
                break

def del_student():
    global students_list
    while True:
        find = input("请输入要删除的学生姓名")
        for i in students_list:
            if i["name"] == find:
                del students_list[students_list.index(i)]
                input("已为您成功删除，按Enter回到主菜单")
                return
        else:
            ctn = input("未找到该学生，是否重新输入并查找？【Y/n】")
            if ctn in ["N", "No", "n", "no"]:
                break



students_list = []
while True:
    print_menu()        # 打印主菜单
    slt = input("请输入您要进行的操作：")

    if slt == "1":
        # 增加
        student_add()    
    elif slt == "2":
        # 查看
        show_students()    
    elif slt == "3":
        # 修改
        modify_students()   
    elif slt == "4":
        # 删除
        del_student()   
    elif slt == "0":
        break