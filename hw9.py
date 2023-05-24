class Point:
    
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
    
    def show(self):
        print(f'{self.__x}, {self.__y}')
        
    def set(self,x,y):
        self.__x = x
        self.__y = y
        
    def get(self):
        return(self.__x,self.__y)
        
class Rectangle:
    
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.__lt = Point(x1,y1)
        self.__rb = Point(x2,y2)
        
    def show(self):
        print(f'\n좌측 상단 꼭지점이 {self.__lt.get()}이고 우측 상단 꼭지점이 {self.__rb.get()}인 사각형입니다.',end='')
        
    def getWidth(self):
        width = self.__rb.get()[0] - self.__lt.get()[0]
        return width
    
    def getHeight(self):
        height = self.__rb.get()[1] - self.__lt.get()[1]
        return height
    
    def getArea(self):
        area = (self.__rb.get()[0] - self.__lt.get()[0])*(self.__rb.get()[1] - self.__lt.get()[1])
        return area
    
    def getPerimeter(self):
        perimeter = (self.__rb.get()[0] - self.__lt.get()[0])*2 + (self.__rb.get()[1] - self.__lt.get()[1])*2
        return perimeter

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
