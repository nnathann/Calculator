import math

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'sqrt': lambda x: math.sqrt(x),
    'sin': lambda x: math.sin(x),
    'cos': lambda x: math.cos(x),
    'avg': lambda x, y: (x + y) / 2,
    'mod': lambda x, y: x % y
}

with open('input.txt') as f:
    for line in f:
        stack = []
        for token in line.strip().split():
            if token in operators:
                try:
                    stack.append(operators[token](*stack[-2:]))
                    stack = stack[:-2]
                except:
                    print(f"Error: Not enough values for '{token}'.")
                    break
            else:
                try:
                    stack.append(float(token))
                except:
                    print(f"Error: Invalid token '{token}'.")
                    break
        if len(stack) == 1:
            print(f"{line.strip()} = {stack[0]}")
        elif len(stack) > 1:
            print("Error: Too many values in the stack.")
        else:
            print("Error: No values in the stack.")
