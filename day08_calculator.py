print('Welcome to the CALCULATOR')
print('='*30)

def calculator():
    while True:
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Invalid input. Please enter numeric values.')
            continue  # Hatalı girişte tekrar sor

        user_input = input('Choose operation (+, -, *, /) or type "exit" to quit: ')
        
        if user_input.lower() == 'exit':
            print('Exiting the calculator. Goodbye!')
            break
        
        if user_input == '+':
            result = num1 + num2
            print(f'The result of {num1} + {num2} = {result}')  
        elif user_input == '-':
            result = num1 - num2
            print(f'The result of {num1} - {num2} = {result}')              
        elif user_input == '*':
            result = num1 * num2
            print(f'The result of {num1} * {num2} = {result}')
        elif user_input == '/':  
            if num2 == 0:
                print('Error: Division by zero is not allowed.')
            else:
                result = num1 / num2
                print(f'The result of {num1} / {num2} = {result}')  
        else:
            print('Invalid operation. Please choose a valid operation.')

calculator()
