a=int(input("input the first number?"))
b=int(input("input the second number?"))
c=int(input("input the third number?"))
max_num=0
if a>b:
    max_num=a
else:
    max_num=b
if c>max_num:
    max_num=c
print(f"the largest number is {max_num}")
''''''
a=int(input("input the first number?"))
b=int(input("input the second number?"))
c=int(input("input the third number?"))
d=int(input("input the fourth number?"))
e=int(input("input the fifth number?"))
max_num=a
if b>max_num:
  max_num=b
if c>max_num:
   max_num=c
if d>max_num:
   max_num=d
if e>max_num:
   max_num=e
print("the largest number is", max_num)
''''''
score=int(input("input score"))
if score>=80:
   print("good")
elif score>=60:
   print ("pass")
elif score<60:
   print("fail")
''''''
a=int(input("input your score"))
if 0<=a<=100:
   if a>=90:
      print("excellent")
   elif a>=80:
      print("good")
   elif a>=60:
      print("passed")
   else:
      print("fail")
else:
     print("error")
''''''
num=int(input("input a number"))
0<=len(str(num))<=3
if len(str(num))==1:
   print("this is a one-digit number")
elif len(str(num))==2:
   print("this is a two-digit number")
else:
   print("this is a three-digit number")
''''''
a=int(input("input a Java score"))
b=int(input("input a Music score"))
if a>98 and b>80:
   print("teacher reward")
elif a==100 and b>70:
   print("teacher reward")
else:
   print("no reward")
''''''
a=int(input("input a Java score"))
b=int(input("input a Music score"))
if a>98 and b>80 or a==100 and b>70:
   print("teacher reward")
else:
   print("no reward")
''''''
a=float(input("input score?"))
gender=input("input a gender?")
if gender=="female" and a<10.0:
   print("reach the female final")
elif gender=="male" and a<10.0:
   print("reach the male final")
else:
   print("failed")
''''''
a=int(input("input a weekday?"))
if a==1:
   print("Monday,eat rice")
elif a==2:
   print ("Tuesday,eat noodles")
elif a==3:
   print("Wednesday,eat mantou")
elif a==4:
   print("Thursday, eat dumplings")
elif a==5:
   print("Friday,eat seafood")
elif a==6:
   print("Saturday,eat hotpot")
elif a==7:
   print("Sunday,eat instant noodles")
else:
   print("error")
''''''
a=int(input("input a number?"))
b=int(input("input another nunber?"))
if a>b:
   print(1)
elif a<b:
   print(-1)
else:
   print(0)
''''''
a=int(input("input a number?"))
b=int(input("input another number?"))
s = input("input an operator (+, -, *, /)")
if s=="+":
   print(a+b)
elif s=="-":
   print(a-b)
elif s=="*":
   print(a*b)
elif s=="/":
    if b!=0:
        print(a/b)
    else:
        print("Error: division by zero")
else:
   print("operator error")
''''''
a=int(input("input a number?"))
b=int(input("input another number?"))
c=int(input("input another number?"))
d=a+b+c
if a>b>c:
  print("the largest nunber is",a, "the smallest number is",c,"the sum is",d)
elif a>c>b:
   print("the largest nunber is",a, "the smallest number is",b,"the sum is",d)
elif b>a>c:
  print("the largest nunber is",b, "the smallest number is",c,"the sum is",d)
elif b<c<a:
  print("the largest nunber is",b, "the smallest number is",a,"the sum is",d)
elif c>a>b:
   print("the largest nunber is",c, "the smallest number is",b,"the sum is",d)  
else:
  print("the largest nunber is",c, "the smallest number is",a,"the sum is",d)
''''''
a=int(input("input a number?"))
b=int(input("input another number?"))
c=int(input("input another number?"))
d=a+b+c
max_num=a
min_num=a
if b>max_num:
    max_num=b
if c>max_num:
    max_num=c
if b<min_num:
    min_num=b
if c<min_num:
    min_num=c
print("the largest nunber is",max_num, "the smallest number is",min_num,"the sum is",d)
''''''
a=int(input("input a number?"))
b=int(input("input another number?"))
c=int(input("input another number?"))
d=a+b+c
print("the largest number is",max(a,b,c))
print("the smallest number is",min(a,b,c))
print("the sum is",d)
''''''
d=int(input("input a number?"))
e=int(input("input another number?"))
f=int(input("input another number?"))
max_num=d
min_num=d
if e>max_num: 
   max_num=e
if f>max_num:
   max_num=f
if e<min_num:
    min_num=e
if f<min_num:
    min_num=f
mid_num=d+e+f-max_num-min_num
print("max:",max_num,"mid:",mid_num,"min:",min_num)
''''''
d=int(input("input a number?"))
e=int(input("input another number?"))
f=int(input("input another number?"))
max_num=max(d,e,f)
min_num=min(d,e,f)
mid_num=d+e+f-max_num-min_num
print(max_num,mid_num,min_num)
''''''
price = float(input("input the price"))
quantity = int(input("input the quantity"))
total = price * quantity
if quantity<5:
    discount_rate=0
elif 5<=quantity<10:
    discount_rate=0.01
elif 10<=quantity<20:
    discount_rate=0.02
elif 20<=quantity<30:
    discount_rate=0.04
elif quantity>=30:
    discount_rate=0.06
final_price=total*(1-discount_rate)
print(f"discount rate:{discount_rate},total price:{total},final price:{final_price}")
# 0.01——1%：{discount_rate*100:.0f}  .0f表示保留0位小数的浮点数（float）格式
''''''
salary=float(input("input a salary?"))
if salary<=2000:
   bonus=0.1*salary
elif 2000<salary<=4000:
   bonus=0.2*salary
elif 4000<salary<=8000:
   bonus=0.3*salary
elif salary>8000:
   bonus=0.4*salary
print(f"salary:{salary},bonus:{bonus}")
''''''
num = input("input a five-digit number?")
if num==num[::-1]:
    print(f"{num}is a palindrome")
else:
    print(f"{num}is not a palindrome")
''''''





   





         
