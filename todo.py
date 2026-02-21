Test=[]
while True:
 print()
 print("1.添加任务")
 print("2.查看任务")
 print("3.退出")
 choice=input("请选择你的操作：(1/2/3)")
 if choice=="1":
    task=input("请写下你要添加的任务：")
    Test.append(task)
    print(f"已添加任务{task}")
 elif choice=="2":
    if not Test:
        print("暂无任务：")
    else:
        print("当前任务:")
        for i,task in enumerate(Test,1):
            print(f"{i}.{task}")    
 elif choice=="3":
    print("再见")
    break
 else:
    print("无效选择，请重新输入：")


