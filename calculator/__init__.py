from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)

class calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        calculation = Calculation(a, b, multiply)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)  # Pass the add function from calculator.operations
        return calculation.get_result()


