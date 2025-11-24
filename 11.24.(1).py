def f1(a,b,c):
    print(max(a,b,c))
f1(2,6,3)

def f2(a,b):
    res=0
    for i in range(a,b+1):
        res+=i
    print(res)
f2(3,6)

def f2(a,b):
    L=[]
    for i in range(a,b+1):
        L.append(i)
    print(sum(L))
f2(3,6)

def f3(a):
    res=1
    for i in range(1,a+1):
        res*=i
    print(res)
f3(6)

def f4(value,list1):
    if value in list1:
        return True
    else:
        return False
print(f4(3,[1,2,4,5,7]))

def f5(*tup):
    res=0
    for i in tup:
        res+=i
    average=res/len(tup)
    return average
print(f5(1,3,6))





       





