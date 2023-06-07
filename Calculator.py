# Challenge 2: Implement a Calculator Class
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print(self.num1 + self.num2)
    def subtract(self):
        print(self.num1 - self.num2)
    def multiply(self):
        print(self.num1 * self.num2)
    def divide(self):
        if self.num2 == 0 :
            print("Cannot divide by zero")
        else:
            print(self.num1 / self.num2)

num1 = int(input('enter yor first number : '))
num2 = int(input('enter yor second number : '))

obj = Calculator(num1,num2)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
