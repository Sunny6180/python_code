
# sum=lambda n:n*(n+1)//2
# print(sum(3))

# L=[1,2,4,6,8,5]
# print(max(L))

# max_value=lambda *nums:max(nums)
# print(max_value(3,7,2,9,5))
#加* 多个参数

# count_value=lambda nums,x:nums.count(x)
# print(count_value([1,4,4,5,7,8],4))


# 编写一个函数，交换指定字典的key和value

# swap_dict = lambda dict:{v: k for k, v in dict.items()}
# dict={"a":2,"b":3}
# print(swap_dict(dict))

# def swap_dict(dict):
#     return{v: k for k, v in dict.items()}

# def swap_dict(dict):
#     new_dict={}
#     for k, v in dict.items():
#         new_dict[v] = k
#     return new_dict

# 5.编写一个函数，提取指定字符串中的所有字母，然后拼接在一起产生一个新的

# def get_letters(s):
#     result=""
#     for a in s:
#         if a.isalpha():     
#             result+=a
#     return result

# def get_letters(s):
#     return "".join([a for a in s if a.isalpha()])

# get_letters=lambda s: "".join(a for a in s if a.isalpha())
# s="abscee24gg"
# print(get_letters(s))

# average=lambda s:sum(s)/len(s)
# s=[1,2,4,6]
# print(average(s))
    

# from functools import reduce
# result=lambda:reduce(lambda x,y:x*y,range(1,11))
# print(result())


# def capitalize(s):
#     return s[0].upper() + s[1:]

# capitalize=lambda s: s[0].upper() + s[1:]
# s="aannnddd"
# print(capitalize(s))

# 写一个自己的 endwith 函数，判断一个字符串是否以指定的字符串结束
# endwith= lambda s,a:True if s[-len(a):]==a else False
# s="134fhd" 
# a="fhd"
# print(endwith(s,a))

# 写一个自己的 rjust 函数，创建一个字符串的长度是指定长度，原字符串在新字符串中右对齐，剩下的部分用指定的字符填充
# rjust=lambda s,a,b:b*(a-len(s))+s
# s="abc"
# a=5
# b="t"
# print(rjust(s,a,b))


# 写一个自己的 index 函数，统计指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1
# index=lambda s,L: "".join(if s in L else -1
# def index(L, x):
#     result=[]
#     for i in range(len(L)):
#         if L[i]==x:
#             result.append(i)
#     return result if result else -1
# # tip:不会用lambda+1
# # index = lambda lst, x: [i for i in range(len(lst)) if lst[i] == x] or -1
# 在 Python 里：
# A or B
# 不是只返回 True 或 False，而是：
# 如果 A 是真值，就返回 A
# 如果 A 是假值，就返回 B
# 什么是“假值”呢？
# Python 中这些都被当成 False：
# 0
# "" 空字符串
# [] 空列表
# {} 空字典
# () 空元组
# False
# None




# 写一个自己的 len 函数，统计指定序列中元素的个数
# def len(L): 
#     count=0
#     for i in L:
#         count+= 1
#     return count
# print(len([1,2,3,4]))

# # tip:序列的长度 =第一个元素的长度 1+剩下所有元素的长度（通过递归计算）
# my_len=lambda seq: sum(1 for _ in seq)
# def my_len(seq):
#     if seq == [] or seq == "":
#         return 0
#     return 1 + my_len(seq[1:])




# # 写一个函数实现自己 in 操作，判断指定序列中，指定的元素是否存在
# exist=lambda s,a:True if a in s else False
# s=[1,2,3,4,8] 
# a=9
# print(exist(s,a))

# def exist(s, x):
#     for i in s:
#         if i==x:
#             return True
#     return False    
# tip:不能用in,还用呢，不会不会不会
# exist = lambda seq, x: False if seq == [] else (True if seq[0] == x else exist(seq[1:], x))




# 14.写一个自己的 replace 函数，将指定字符中指定的旧字符串转换成指定的新字符串
# 15.写一个自己的 max 函数，获取指定序列中元素的最大值，如果序列是字典，取字典值的最大值
# 例如：序列：[-1, -12, -1, -9] 结果：-1 序列：‘abcdpzasdz’ 结果：‘z’ 序列：{‘小明’: 90, ‘张三’: 76, ‘路飞’: 30, ‘小花’: 98} 结果：98

