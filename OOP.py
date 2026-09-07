from random import randint
import turtle


class Point:
  
    #坐标信息
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #判断点是否在矩形内
    def falls_in_rectangle(self, rectangle_area):
        return rectangle_area.point1.x < self.x < rectangle_area.point2.x \
            and rectangle_area.point1.y < self.y < rectangle_area.point2.y


class Rectangle:
    
    #确保左下角和右上角坐标无误
    def __init__(self, point1, point2):
        self.point1 = Point(min(point1.x, point2.x), min(point1.y, point2.y))
        self.point2 = Point(max(point1.x, point2.x), max(point1.y, point2.y))

    #算出猜测的矩形面积与实际面积的偏差
    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    #画出矩形
    def draw(self, canvas):
        canvas.penup()                                  #抬笔
        canvas.goto(self.point1.x, self.point1.y)       #移到左下角

        canvas.pendown()                                #落笔
        canvas.forward(self.point2.x - self.point1.x)   #向前画一条线
        canvas.left(90)                                 #左转90度
        canvas.forward(self.point2.y - self.point1.y)   #向前画一条线
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
   
    #画出猜测的点
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()                  #抬笔
        canvas.goto(self.x, self.y)     #移到点的位置

        canvas.pendown()                #落笔
        canvas.dot(size, color)         #绘制点

        turtle.done()                   #告诉 turtle 画完了，保持窗口不关闭，等待用户操作


#创建坐标
rectangle = GuiRectangle(Point(randint(0, 200), randint(0, 200)),
                         Point(randint(10, 200), randint(10, 200)))

#输出已定的框架信息
print("矩形的左上角:(",
      rectangle.point1.x, ",",
      rectangle.point1.y,")","   矩形的右下角:(",
      rectangle.point2.x, ",",
      rectangle.point2.y, ")")

#用户输入猜测的点和面积
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess 矩形面积: "))

#输出结果
print("你的点在矩形内: ", user_point.falls_in_rectangle(rectangle))
print("你输入的面积与实际面积相差: ", abs(rectangle.area() - user_area))

myturtle = turtle.Turtle()  #创建turtle对象，可类似为一支画笔
rectangle.draw(myturtle)
user_point.draw(myturtle)
