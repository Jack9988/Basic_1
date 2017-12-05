"""
功能：五角星的绘制
版本：v3.0
作者：杰克
时间：2017年11月16日23:21:32
新增功能：增加循环操作
新增功能：使用迭代函数绘制

"""

import turtle

def draw_recursive_pentagram(size):
    """
    迭代绘制,递归函数，自身调用自身来改变参数值。
    :param size:
    :return:
    """
    #计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

    #五角星绘制完成,更新参数
    size+=10
    if size<=100:
        draw_recursive_pentagram(size)

def main():
    """
        主函数
    """
    size=50
    draw_recursive_pentagram(size)

    turtle.exitonclick()

if __name__=='__main__':
    main()
