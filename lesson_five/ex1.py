def solve_for_x(string):
    x, op, num1, eq, num2 = string.split()
    
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        op = '-'
        result = num2 - num1

    elif op == '-':
        op = '+'
        result = num2 + num1

    print("{} {} {} {} {}".format(x, eq, num2, op, num1))
    print("x = ", result)


string = input("Enter string: ")

solve_for_x(string)
