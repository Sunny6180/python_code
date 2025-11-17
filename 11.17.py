dic = {'python': 95,'java': 99,'c': 100}
print(len(dic))
dic['java']=98
del dic['c']
dic['php']=90
keys_list=list(dic.keys())
print(keys_list)
values_list=list(dic.values())
print(values_list)
print('javascript' in dic)
print(sum(dic.values()))
print(max(dic.values()))
print(min(dic.values()))
dic1={'php':97}
dic.update(dic1)
print(dic)


fruit_price={"苹果": 32.8,"香蕉": 22,"葡萄": 15.5}
name = input("input fruit name:")
if name in fruit_price:
    print(f"{name} 的价格是:{fruit_price[name]}元")
else:
    print("error")
print("input count:")
apple_count=int(input("苹果数量:"))
banana_count=int(input("香蕉数量:"))
grape_count=int(input("葡萄数量:"))
total=apple_count*fruit_price["苹果"]+banana_count*fruit_price["香蕉"]+grape_count*fruit_price["葡萄"]
print(f"总价格为:{total}元")


