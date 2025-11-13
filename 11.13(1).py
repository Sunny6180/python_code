# a = [1,2,3,4,5]
# result=sum(a)
# print(result) 

# a=[]
# while True:
#     num=int(input("input a number"))
#     if num==0:
#         break
#     if num not in a:
#         a.append(num)
#         print("added:",num)
#     else:
#         print("repeat")
#     total=sum(a)
#     print(total)


# scores=[] 
# for i in range(6):
#     a=float(input(f"请输入第 {i+1} 位评委的打分:")) 
#     scores.append(a)
# print("所有分数：", scores)
# scores.remove(max(scores))
# scores.remove(min(scores))
# print("去掉最高分和最低分后的分数:",scores)
# final_score = sum(scores)/len(scores)
# print("选手的最终成绩为:",final_score)

# c = ["辽宁省","大连市","高新区","科技创业大厦"]
# result=[]
# for a in c:
#     result.append(a)
# print(*c, sep="")
# ''''''
# c = ["辽宁省", "大连市", "高新区", "科技创业大厦"]
# result = "".join(c)
# print(result)

# b = ["我", "爱", "你", "中", "国"]
# result = ",".join(b)
# print(result)
# tip:用逗号，把 b 里的所有元素串起来

# a=0
# list1=[1,3,4,5,0,0,6,6,0,5,4,7,6,7,0,5]
# for i in list1:
#         if i==0:
#               a+=1
# print(a)

# a=0 
# list1=[60,59,77,53,66,12]
# for i in list1:
#     if i>=60:
#         a+=1
# print(a)

# a=0
# b=0
# list1=[-60,59,-77,53,66,-12]
# for i in list1:
#     if i>0:
#         a+=i 
#     elif i<0:
#         b+=i
# print(a,b)

# old_list=[1,0,3,4,2,0,7,0,5]
# new_list=[]
# for i in old_list:
#     if i!=0:
#         new_list.append(i)
# print(new_list)


# list1=[]
# while True:
#     print("welcome to contact app:")
#     print("choose your menu:\n1.Add \n2.Update \n3.Delete \n4.Query \n5.Exit")
#     choose=input("please input menu number")
#     if choose=="1":
#         print("Add a number")
#         a=int(input("input a number"))
#         if a not in list1:
#             list1.append(a)
#             print("added successfully")
#     elif choose=="2":
#         print(list1)
#         b=int(input("input the number to modify"))
#         if b not in list1:
#             print("error,try again")
#         else:
#             index=list1.index(b)
#             c=int(input("input new number"))
#             list1[index]=c
#             print("update successfully")
#     elif choose=="3":
#         print(list1)
#         d=int(input("choose the number to delete"))
#         if d not in list1:
#             print("error,try again")
#         else:
#             list1.remove(d)
#             print("delete successfully")
#     elif choose=="4":
#         for i in range(len(list1)):
#             print(i,list1[i])
#     elif choose=="5":
#         print("exit")
#         break
#     else:
#         print("wrong menu number,try again")



#输入某年某月某日，判断这一天是这一年的第几天？
a=int(input("input year number"))
b=int(input("input month number"))
c=int(input("input day number"))
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
if (a%4==0 and a%100!=0)or(a%400==0):
    days_in_month[1]=29
total_days = sum(days_in_month[:b-1])+c
print("这一天是这一年的第", total_days, "天")

