# Classes are user defined blueprint or prototype
# Variables and operations e.g. Addition, Subtraction, Multiplication, Division, Mod etc. / Constants declared
# Classes may have class/instance variables, methods/constructor, objects for your classes etc
# Constructor is a method which is called when its object is created

# Self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100  # Class variables

    # when no constructor is defined, default constructor was called

    def __init__(self, a, b):  # Default constructor converted to parameterized constructor
        self.firstNumber = a  # Instance variable
        self.secondNumber = b  # Instance variable
        print("I am called automatically when the object is created.")

    def getData(self):
        print("I am now executing as method in the class")

    def Summation(self):
        # return self.firstNumber + self.secondNumber
        # return self.firstNumber + self.secondNumber + num - Only class variable cannot be called
        # return self.firstNumber + self.secondNumber + Calculator.num - Use <ClassName.ClassVariable>
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)  # Creating object of a class, which calls constructor automatically
obj.getData()  # accessing method using the object created
print(obj.num)  # accessing variable using the object created
print(obj.Summation())

obj1 = Calculator(7, 8)  # Creating object of a class, which calls constructor automatically
obj1.getData()  # accessing method using the object created
print(obj1.num)  # accessing variable using the object created
print(obj1.Summation())
