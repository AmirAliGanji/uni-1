num=str(input('please enter a number:'))
count=0
for i in num:
    count+=1
print(count)    
    
#%%         seh add begirad va az bozorg be koochack moratab konad
num1=int(input('please enter a number:'))
num2=int(input('please enter a number:'))
num3=int(input('please enter a number:'))
max_num = num1
mian=num2
min_num = num3

if num2>max_num:
    max_num=num2    

elif num3> max_num:
    max_num=num3    

else:
    max_num=num1   

if num1<min_num:
    min_num=num1

elif num2<min_num:
    min_num = num2

else:
    min_num = num3

if num1<max_num & num1>min_num:
    mian=num1

elif num2 <max_num & num2>min_num:
    mian=num2

else:
    mian=num3
print(max_num,mian,min_num)