#Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
         return (print(self.x**2 + self.y**2 + self.z**2))
        

obj = Point(1,3,5)
obj.sqSum()