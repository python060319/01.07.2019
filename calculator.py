# input 2 numbers (outside the loop)

# print message: + - * / Q
# input operation from user
# + : will print the sum - : will print the subtraction
# if user entered something else : continue
# if user divide by zero : i.e. 5 0 / : break
# run until user entered 'Q' (or break divide by zero)

# choose between while and do-while....


x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
oper = ''
while oper.upper() != 'Q':
    oper = input("Enter operation + - / * Q: ")
    if oper in ['+', '-', '*', '/'] == False:
        continue
    if oper == '/' and y == 0:
        print("cannot divide by zero....")
        break
    if oper == '+':
        print(f'{x} + {y} = {x + y}')
        #print(x, '+', y, x+y)
        #print(x + ' + ' + y + ' = ' + (x +y))
    elif oper == '-':
        print(f'{x} - {y} = {x - y}')
    elif oper == '*':
        print(f'{x} * {y} = {x * y}')
    elif oper == '/':
        print(f'{x} / {y} = {x / y}')
