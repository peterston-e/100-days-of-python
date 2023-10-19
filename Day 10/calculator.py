# calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# we are going to call it like so:
# function = operation["+"]
# function(2, 3)


def calculator():
    num1 = int(input("whats the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("whats the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(
            f"type 'y' to continue with {answer} or type 'n' to start a new calculation.: ")
        if continue_calc == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
