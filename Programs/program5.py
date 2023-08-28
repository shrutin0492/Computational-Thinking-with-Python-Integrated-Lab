# 5.
# Create an interactive calculator. User input is assumed to be a formula that consist of a number, an operator
# (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

# a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.

# b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError

# c. If the second input is not '+' or '-', again raise a FormulaError

# d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

class FormulaError(Exception):
    pass

def perform_calculation(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

def main():
    while True:
        user_input = input("Enter a formula (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting the calculator.")
            break

        try:
            elements = user_input.split()
            if len(elements) != 3:
                raise FormulaError("Invalid input: A formula should consist of 3 elements.")

            num1 = float(elements[0])
            num2 = float(elements[2])
            operator = elements[1]

            if operator not in ['+', '-']:
                raise FormulaError("Invalid operator: Only '+' and '-' operators are allowed.")

            result = perform_calculation(num1, operator, num2)
            print(f"Result: {result}")

        except ValueError:
            print("Error: Invalid number format.")
        except FormulaError as fe:
            print(f"Formula Error: {fe}")

if __name__ == "__main__":
    main()
