class Calculator:
    def _init_(self, a: float, b: float, type_of_operation: str):
        self.a = a
        self.b = b
        self.type_of_operation = type_of_operation.lower()

    def calculate(self):
        if self.type_of_operation == "add":
            return self.a + self.b

        elif self.type_of_operation == "sub":
            return self.a - self.b

        elif self.type_of_operation == "mul":
            return self.a * self.b

        elif self.type_of_operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"

        else:
            return "Invalid operation type"
