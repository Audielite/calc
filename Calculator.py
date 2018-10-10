numbers = (int, float, complex)

class Calculator:

    @staticmethod
    def calculations(a, b):
        if not isinstance(a, numbers) and not isinstance(b, numbers):
            raise ValueError

    def multiplication(self, a, b):
        self.calculations(a, b)
        return a * b

    def division(self, a, b):
        self.calculations(a, b)
        return a / b

    def addition(self, a, b):
        self.calculations(a, b)
        return a + b

    def subtraction(self, a, b):
        self.calculations(a, b)
        return a - b


'''print("Select 1 for multiplication")
    print("Select 2 for division")
    print("Select 3 for addition")
    print("Select 4 for subtraction\n")

    selection = (input("Choose calculation: "))

    choice = int(input("\nNumber: "))
    choice2 = int(input("Number: "))

    if selection == '1':
        print(choice, "*", choice2, "=", (choice * choice2))

    elif selection == '2':
        print(choice, "/", choice2, "=", (choice / choice2))

    elif selection == '3':
        print(choice, "+", choice2, "=", (choice + choice2))

    elif selection == '4':
        print(choice, "-", choice2, "=", (choice - choice2))

    else:
        print("Please choose a valid option.")'''
