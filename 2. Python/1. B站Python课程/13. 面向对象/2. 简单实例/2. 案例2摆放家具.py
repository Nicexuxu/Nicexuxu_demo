# 需求：
# 1.房子(House)有户型、总面积和家具名称列表
# 新房子没有任何的家具
# 2.家具(Houseltem) 有 名字 和 占地面积，其中
# 席梦思(bed)占地 4平米
# 衣柜(chest)占地 2平米
# 餐桌(table) 占地 1.5 平米。
# 3.将以上三件 家具 添加 到 房子 中
# 4.打印房子时，要求输出:户型、总面积、剩余面积、家具名称列表
class HouseItem:
    def __init__(self, name, area) -> None:
        self.name = name
        self.area = area
    def __str__(self) -> str:
        return "%s占地%s平米" % (self.name, self.area)
# 创建家具
HOUSEITEM_bed = HouseItem("席梦思", 15)
HOUSEITEM_chest = HouseItem("衣柜", 10)
HOUSEITEM_table = HouseItem("餐桌", 5)
print(HOUSEITEM_bed, HOUSEITEM_chest, HOUSEITEM_table)

print("fengexian" * 15)

class House:
    def __init__(self, house_type, area) -> None:           # 创建初始属性
        self.house_type = house_type
        self.area = area
        self.free_area = self.area
        self.item_list = []
    def __str__(self) -> str:                               # str方法打印房子信息
        return ("户型：%s\n总面积：%.2f（剩余：%.2f）\n家具：%s"
                 % (self.house_type, self.area,
                    self.free_area,  self.item_list))
    def add(self, houseitem):
        print("添加%s" % houseitem.name)
        if houseitem.area > HOUSE_myhouse.free_area:        # 如果家具占地面积大于剩余面积，则无法添加
            print("%s的面积太大了，无法添加" % houseitem.name)
        else:
            self.item_list.append(houseitem.name)
            self.free_area -= houseitem.area
            print("%s添加成功，剩余面积%.2f" % (houseitem.name, self.free_area))    # 成功添加

HOUSE_myhouse = House("两室一厅", 50)
print(HOUSE_myhouse)
HOUSE_myhouse.add(HOUSEITEM_bed)
HOUSE_myhouse.add(HOUSEITEM_chest)
HOUSE_myhouse.add(HOUSEITEM_table)
print(HOUSE_myhouse.item_list)