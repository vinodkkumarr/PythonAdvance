
class Calculator:

    def __init__(self, a, b):
        self.FirstNumber = a
        self.SecondNumber = b

    def addition(self):
        print(self.FirstNumber + self.SecondNumber)
        return self

    def subtraction(self):
        print(self.FirstNumber - self.SecondNumber)
        return self

    def multiplication(self):
        print(self.FirstNumber * self.SecondNumber)
        return self

    def divide(self):
        try:
            print(self.FirstNumber / self.SecondNumber)
        except:
            print("An exception occurred")


c = Calculator(10, 20)

print(c.addition().subtraction().multiplication().divide())

# fn chaining


def calculate(a, b):

    print("First number is :" + str(a))
    print("Second number is :" + str(b))

    def compare(operation):
        if operation == "add":
            print("Addition of entered number is: {}" .format(a + b))
        elif operation == "sub":
            print("Subtraction of entered number is: {}" .format(a - b))
        elif operation == "multiply":
            print("Multiplication of entered number is: {}" .format(a * b))
        elif operation == "divide":
            print("Divison of entered number is: {}".format(a / b))
        else:
            print("Not a valid operation")

    return compare


c = calculate(10, 20)
c("add")
c("sub")
c("multiply")
c("divide")
#c("d")





