# Challenge 3: Implement the Complete Student Class

class Student:

    __name = "vishal"
    __rollNumber = 12345

    def setName(self,nm):
        self.name=nm
    def getName(self):
        print("this name is: ",self.name)
    def setRollNumber(self,num):
        self.rollNum = num
    def getRollNumber(self):
        print("this roll number is: ",self.rollNum)

obj = Student()
print(obj._Student__name)
print(obj._Student__rollNumber)
obj.setName(input("Enter your name: "))
obj.getName()
obj.setRollNumber(int(input('enter your roll number:')))
obj.getRollNumber()
