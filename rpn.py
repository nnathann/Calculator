import math

# Define the supported operators and their corresponding functions
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

# Open the input file
with open('input.txt') as f:
    # Process each line in the file
    for line in f:
        stack = []  # Create an empty stack to store values
        # Split the line into individual tokens and process each token
        for token in line.strip().split():
            if token in operators:  # If the token is an operator
                try:
                    # Apply the operator to the last two values in the stack
                    # and append the result to the stack
                    stack.append(operators[token](*stack[-2:]))
                    # Remove the last two values from the stack
                    stack = stack[:-2]
                except:
                    # Handle errors when applying the operator
                    print(f"Error: Not enough values for '{token}'.")
                    break
            else:  # If the token is not an operator (assume it's a number)
                try:
                    # Convert the token to a float and append it to the stack
                    stack.append(float(token))
                except:
                    # Handle errors when converting the token to a float
                    print(f"Error: Invalid token '{token}'.")
                    break
        if len(stack) == 1:
            # If there is exactly one value in the stack, print it as the result
            print(f"{line.strip()} = {stack[0]}")
        elif len(stack) > 1:
            # If there are more than one value in the stack, it's an error
            print("Error: Too many values in the stack.")
        else:
            # If there are no values in the stack, it's an error
            print("Error: No values in the stack.")
