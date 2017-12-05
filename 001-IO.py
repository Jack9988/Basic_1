#文字输出print()
print("Hello,World!")

print('The quick brown fox', 'jumps over', 'the lazy dog',123)

name="Jack"
weight=64
height=170
age=28
print("{0}的体重是{1}kg,身高是{2}cm，年龄是{3}岁.".format(name,weight,height,age))

#内容输入input()，接收的是字符串str
name=input("请输入你的名字：")

age=int(input("请输入您的年龄："))
weight=float(input("请输入您的身高："))
print(age,weight)
