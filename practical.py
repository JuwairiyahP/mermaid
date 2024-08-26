'''
#22
l=eval(input("Enter list:"))
a=int(input("Enter element:"))
count=0
for i in l:
    if a==i:
        count+=1
print("Count is",count)
'''
'''
#23
l=eval(input("Enter list:"))
sumofeven=0
sumofodd=0
for i in range(len(l)):
    if i%2==0:
        sumofeven+=l[i]
    else:
        sumofodd+=l[i]
print("sum of even index numbers-sum of odd index numbers=",sumofeven-sumofodd)
'''
'''
#24
t=0,
s1=0
s2=1
n=int(input("Enter number of elements:"))
for i in range(n):
    s3=s2+s1
    s1=s2
    s2=s3
    t=t+(s1,)
print(t)
'''
'''
#25
t=eval(input("enter tuple:"))
l=sl=t[0]
for i in t:
    if i>l:
        sl=l
        l=i
    elif i>sl:
        sl=i
print("second largest number is",sl)
'''
'''
#26
dic={}
choice='y'
while choice=='y':
    product=input("enter product:")
    price=float(input("enter price:"))
    dic[product]=price
    choice=input("enter \'y\' to continue adding:")
print(dic)
choice='yes'
while choice=='yes':
    product=input("enter product to search for:")
    print("its price is",dic[product])
    choice=input("enter \'yes\' to continue searching:")
'''