print('Hello there! Welcome to SuperCalc\n'
      'You are gonna create a simple calculator like a pro by entering any two numbers and a mathematical sign of '
      'your choice')


def supercalc():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    op_sign = input('Enter a mathematical operation: ')
    if op_sign == '+':
        result = num1 + num2
    elif op_sign == '-':
        result = num1 - num2
    elif op_sign == '*':
        result = num1 * num2
    elif op_sign == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Can't divide by zero")
            return
    elif op_sign == '**':
        result = num1 ** num2
    elif op_sign == '//':
        result = num1 // num2
    elif op_sign == '%':
        result = num1 % num2
    else:
        print('Invalid operator!')
        return
    print(f'{num1} {op_sign} {num2} = {result}')


supercalc()
