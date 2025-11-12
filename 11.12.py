# for i in range(1,7):
#     print(i)

# for i in range(2,11,2):
#     print(i)

# n=1
# while n<=32:
#     print(n)
#     n*=2

# n=1
# for i in range(6):
#     print(n)
#     n*=2

# n=1
# for i in range(6):
#     print(n)
#     n/=2

# for i in range(6):
#     print(f"1/{2**i}")
#     #打印分数

# n=1
# while n<=100:
#     if n%7==0:
#         print(n)
#     n+=1

# for i in range(1,101):
#     if i%2==0 and i%3==0 and i%7==0:
#         print(i)

# n=1
# sum=0
# while n<=5:
#     n+=1
#     sum+=n
# print(sum)

# a=int(input("enter a number"))
# b=int(input("enter another number"))
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(sum)

# expression = " + ".join(str(i) for i in range(a, b + 1)) 加法表达式
#print(f"结果：{sum} ({expression} = {sum})")

# sum_1=0
# sum_2=0
# for i in range(1,101,2):
#     sum_1+=i
# for i in range(-100,0,2):
#     sum_2+=i
# print(sum_1+sum_2)

# for i in range(100,1001):
#     a=i//100
#     b=i%100//10
#     c=i%10
#     if i%(a+b+c)==0:
#        print(i)

# for i in range(100,1001):
#     a=i//100
#     b=i%100//10
#     c=i%10
#     if i==a**3+b**3+c**3:
#         print(i)

# sum=1
# for i in range(1,8):
#     sum*=i
# print(sum)

# a=int(input("input a number"))
# sum=1
# for i in range(1,a+1):
#     sum*=i
# print(sum)

# a=int(input("input a number"))
# b=int(input("input another number"))
# sum=1
# for i in range(a,b+1):
#     sum*=i
# print(sum)


#鸡兔同笼问题，35个头，94只脚，鸡兔各多少只？

# for i in range(1,36):
#     a=35-i
#     if 2*a+i*4==94:
#         print(i,a)
    

# a=int(input("input a number"))
# b=int(input("input a number"))
# c=int(input("input a number"))
# d=int(input("input a number"))
# e=int(input("input a number"))
# sum_1=0
# sum_2=0
# for i in [a,b,c,d,e]:#此为遍历
#     if i>0:
#         sum_1+=i
#     elif i<0:
#         sum_2+=i
# print(sum_1,sum_2)


# sum_p=0  
# sum_n=0  
# for i in range(5): 
#     num = int(input(f"请输入第 {i+1} 个数字: "))
#     if num>0:
#         sum_p+=num
#     elif num<0:
#         sum_n+=num
# print(sum_p,sum_n)



    


