a = [("bicyle", 1500), ("caeffe", 30), ("book", 80), ("desk", 1000), ("iphone",8000), ("xiaomi", 1800)]
b = []
salary = input("请输入工资")
if salary.isdigit():
    salary = int(salary)
    while True:
        for k, v in enumerate(a, 1):
            print(k, v)
        choose = input("选择商品[输入：q退出]>>>")
        if choose.isdigit():
            choose = int(choose)
            if choose < 0 or choose >len(a):
                print("选择错误")
            else:
                if a[choose][1] > salary:
                        print("工资不够，差：", b[int(choose)] - int(salary), "元")

                elif a[choose][1] <= salary:
                    item = a[choose-1]
                    b.append(item)
                    salary = salary-a[choose-1][1]
                    print("剩余工资%s"% salary)
        elif choose == 'q':
            print("----------已购买商品-----------")
            for k, v in enumerate(b, 1):
                print(k, "价格：", v)
        else:
            print("invalid input")

else:
    print("不合法输入")
