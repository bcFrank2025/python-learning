print("简单计算器")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")
choice=input("请选择运算类型(1/2/3/4)：")
a=float(input("清输入第一个数字："))
b=float(input("清输入第二个数字："))

if choice =="1":
   result=a+b
   print(f"结果：{a}+{b}={result}")
elif choice =="2":
   result=a-b
   print(f"结果：{a}-{b}={result}")
elif choice =="3": 
   result=a*b
   print(f"结果：{a}*{b}={result}")  
elif choice =="4": 
   try:   
      result=a/b
      print(f"结果：{a}/{b}={result}")
   except ZeroDivisionError:
      print("错误：除数不能为0！")
else:
   print("无效选择！")
        
      

