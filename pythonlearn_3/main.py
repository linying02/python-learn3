#列表的定义与索引
# list_1 = ["山","东","科","技","大","学"]
# print(list_1)
# print(list_1[1])
#列表尾部追加元素
# list_1 = ["山","东","科","技","大","学"]
# list_1.append("第一")
# print(list_1)
#将列表别的数据容器的元素取出追加到列表最后
# list_1 = ["山","东","科","技","大","学"]
# list_2 = ["第","一"]
# list_1.extend(list_2)
# print(list_1)
#向列表插入一个元素，不会覆盖原先的元素
# list_1 = ["山","东","科","技","大","学"]
# list_1.insert(0,"111")
# print(list_1)
#查找元素在列表中的索引下标
# list_1 = ["山","东","科","技","大","学"]
# mun = list_1.index("东")
# print(mun)
#统计此元素在列表中出现的次数
# list_1 = ["东","东","科","技","东","学"]
# mun = list_1.count("东")
# print(mun)
#统计列表中元素的总个数
# list_1 = ["东","东","科","技","东","学"]
# mun = len(list_1)
# print(mun)
#删除列表指定下表元素
#方法一
# list_1 = ["东","东","科","技","东","学"]
# del list_1[2]
# print(list_1)
#方法二
# list_1 = ["东","东","科","技","东","学"]
# num = list_1.pop(2)
# print(num)
# print(list_1)
#从前往后，删除元素的第一个匹配项
# list_1 = ["东","东","科","技","东","学"]
# list_1.remove("科")
# print(list_1)
#清空列表
# list_1 = ["东","东","科","技","东","学"]
# list_1.clear()
# print(list_1)
#练习案例:使用循环语句取出列表中的偶数
# list_1 = [1,5,6,32,5,5,8,1,5,1,15,41,5,5,245,14,6,4,6]
# list_2 = []
# num = 0
# while num < len(list_1):
#     if list_1[num]%2 == 0:
#         number = list_1[num]
#         list_2.append(number)
#     num+=1
# print(list_2)

# list_1 = [1,5,6,32,5,5,8,1,5,1,15,41,5,5,245,14,6,4,6]
# list_2 = []
# for i in list_1:
#     if i%2 == 0:
#         list_2.append(i)
# print(list_2)

