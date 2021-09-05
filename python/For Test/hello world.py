# -*- coding:utf-8  -*-

height=float(input("请输入您的身高："))
weight=float(input("请输入您的体重："))
bmi=weight/(height*weight)

if bmi<18.5:
    print("您的BMI指数为："+str(bmi))      #输出BMI指数
    print("体重过轻 ~@_@~")
if bmi>=18.5 and bmi <24.9:
    print("您的BMI指数为："+str(bmi))
    print("正常范围，注意保持！")
if bmi>=24.9 and bmi < 29.9:
    print("您的BMI指数为："+str(bmi))
    print("体重过重！")
if bmi>=29.9:
    print("您的BMI指数为："+str(bmi))
    print("您过于肥胖，请注意减肥！")