# Simple Calculator

# add
def add(n1, n2):
    return n1 + n2

# substract
def substract(n1, n2):
    return n1 - n2

# divide
def divide(n1, n2):
    return n1 / n2

# multiply
def multiply(n1, n2):
    return n1 * n2

operations = {
    '+': add,
    '-': substract,
    '/': divide,
    '*': multiply
}

def calculator():

    number1 = float(input('What is the first number?:'))
    for i in operations:
        print(i)
    is_continue = True

    while is_continue:
        operation_name = input('Choose an action from the above:')
        number2 = float(input('What is the second number?:'))
        calculation_function = operations[operation_name]
        answer = calculation_function(number1, number2)

        print(f'{number1} {operation_name} {number2} = {answer}')

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            number1 = answer
        else:
            is_continue = False
            calculator()

calculator()



