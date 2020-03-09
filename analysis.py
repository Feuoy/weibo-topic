import random
import xlrd
import excelSave as save
import os
import jieba
from snownlp import SnowNLP

# 插入文本到txt中
def insertToTxt(content, fileName):
    with open(fileName, "a", encoding='utf-8') as file:
        file.write(content + ",")

# 插入xls
def insert_data(elems,sentiments_temp):
    path = "test4.xls"
    for index,elem in enumerate(elems):
        workbook = xlrd.open_workbook(path)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        rid = rows_old
        # 热词
        word = elem[0]
        # 词频
        frequency = elem[1]
        # 情绪
        emotion = sentiments_temp[index]

        if frequency >= 3 and float(emotion) >= 0.7:
            value1 = [
                [rid, word,frequency,emotion], ]
            print("当前插入第%d条数据" % rid)
            save.write_excel_xls_append_norepeat("test4.xls", value1)

file = open('test2.txt',errors="ignore",encoding="utf-8")
file_context = file.read()
words1 = jieba.lcut(file_context)  # 全模式
words2 = jieba.lcut_for_search(file_context)  # 搜索引擎模式

# 统计词频
data1 = {}
for chara in words1:
    if len(chara) < 2:
        continue
    if chara in data1:
        data1[chara] += 1
    else:
        data1[chara] = 1
data1 = sorted(data1.items(), key=lambda x: x[1], reverse=True)  # 排序

data2 = {}
for chara in words2:
    if len(chara) < 2:
        continue
    if chara in data2:
        data2[chara] += 1
    else:
        data2[chara] = 1
data2 = sorted(data2.items(), key=lambda x: x[1], reverse=True)  # 排序

print("----------")

# 放存入txt的，词语*频次列表
txt_context = []
# 放存入txt的，情感词列表
sentiments_temp = []

print("---褒义---")
print('词语：           频次：       情感值：' )
for i in data2:
    s1 = SnowNLP(i[0])
    sentiments_temp.append(str(round(s1.sentiments,2)))
    try:
        if i[1] >= 10 and s1.sentiments >= 0.7:
            # 打印
            print(i[0] +  '           ' + str(i[1]) + '              ' + str(round(s1.sentiments,2)))
            # 存txt
            for j in range(i[1]):
                txt_context.append(str(i[0]))
    except ValueError:
        pass

#存txt
random.shuffle(txt_context)
txt_str = ''
for i in txt_context:
    txt_str = txt_str + i + "，"
insertToTxt(txt_str, 'test3.txt')
print("存txt，ok")

# 存xls
if os.path.exists("test4.xls"):
    print("文件已存在")
else:
    print("文件不存在，重新创建")
    value_title = [["rid", "热词", "词频", "情感值"],]
    save.write_excel_xls("test4.xls", "统计数据", value_title)
insert_data(data2,sentiments_temp)
print("存xls，ok")