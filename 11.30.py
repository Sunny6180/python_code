
# import myshape

# myshape.triangle(3, 4, 5)
# myshape.rectangle(5, 2)
# myshape.square(4)
# （无法运行？）



# import pandas as pd

# df = pd.DataFrame({
#     "name": ["Jeff", "Rose", "Jack", "Barry"],
#     "age": [28, 20, 19, 32],
#     "city": ["DL", "BJ", "DL", "BJ"],
#     "score": [93.5, 92.5, 93.5, 93.5],
#     "class": [1, 2, 3, 4]
# })

# df.to_csv("test.csv", index=False)







# 按照不同city所在地,保存成不同的文件,也是csv格式 ,文件格式如下
# name,age,score,class
# Jeff,28,93.5,1
# Rose,20,86.5,2
# Jack,19,65,3
# Barry,32,98,4

# import pandas as pd
# df = pd.DataFrame({
#     "name": ["Jeff", "Rose", "Jack", "Barry"],
#     "age": [28, 20, 19, 32],
#     "city": ["DL", "BJ", "DL", "BJ"],
#     "score": [93.5, 92.5, 93.5, 93.5],
#     "class": [1, 2, 3, 4]
# })

# for city in df["city"].unique():
#     sub_df = df.query("city == @city").drop(columns="city")
#     sub_df.to_csv(f"{city}.csv", index=False)


# import pandas as pd

# df = pd.DataFrame({
#     "name": ["Jeff", "Rose", "Jack", "Barry"],
#     "age": [28, 20, 19, 32],
#     "city": ["DL", "BJ", "DL", "BJ"],
#     "score": [93.5, 92.5, 93.5, 93.5],
#     "class": [1, 2, 3, 4]
# })

# # 遍历所有城市
# cities = df["city"].unique()

# for c in cities:
#     sub_df = df[df["city"] == c].drop(columns=["city"])
#     sub_df.to_csv(f"{c}.csv", index=False)



# from datetime import datetime

# d = datetime(2019,12,14)
# print(d.strftime("%Y年%m月%d日"))

# from datetime import datetime,timedelta

# today=datetime.today()

# def fmt(date):
#     return date.strftime("%Y年%m月%d日")

# print("今天：",fmt(today))

# print("明天：",fmt(today+timedelta(days=1)))

# print("昨天：",fmt(today-timedelta(days=1)))

# print("前天：",fmt(today-timedelta(days=2)))

# print("下星期：",fmt(today+timedelta(days=7)))

# if today.month==12:
#     next_month=today.replace(year=today.year+1, month=1)
# else:
#     next_month=today.replace(month=today.month+1)

# print("下个月：",fmt(next_month))
# print("明年：", fmt(today.replace(year=today.year+1)))
# print("去年：", fmt(today.replace(year=today.year-1)))

# 输出本机 python.exe所在的路径
import os, sys
print(os.path.realpath(sys.executable))






# import sys
# print(sys.executable)
