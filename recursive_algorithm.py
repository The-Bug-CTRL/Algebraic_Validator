def is_operator(char):
    # Check if the character is one of the basic operators (+, -, *, /)
    return char in ['+', '-', '*', '/']

def is_valid_operand(operand):
    try:
        # Try to convert the operand to a float to check if it's a valid numeric value
        float(operand)
        return True
    except ValueError:
        # If the conversion fails, it's not a valid operand
        return False

def evaluate_expression(expression):
    def perform_operation(operator, operand1, operand2):
        # Perform the specified arithmetic operation
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            # Check for division by zero
            if operand2 != 0:
                return operand1 / operand2
            else:
                raise ValueError("Division by zero")

    def evaluate_helper(start, end):
        # Recursively evaluate the expression within the specified range

        # Extract the substring representing the operand
        operand = expression[start:end + 1]

        # Check if the operand is a valid numeric value
        if is_valid_operand(operand):
            return float(operand)

        # Initialize variables for operator index and parentheses count
        operator_index = -1
        paren_count = 0

        # Search for the rightmost addition or subtraction operator not inside parentheses
        for i in range(end, start - 1, -1):
            if expression[i] == ')':
                paren_count += 1
            elif expression[i] == '(':
                paren_count -= 1

            # If outside parentheses and operator is found, set operator_index and break
            if paren_count == 0 and (expression[i] == '+' or expression[i] == '-'):
                operator_index = i
                break

        # If no addition or subtraction operator is found, search for other operators or parentheses
        if operator_index == -1:
            for i in range(end, start - 1, -1):
                if expression[i] == ')':
                    i = expression.find('(', 0, i)
                elif expression[i] == '(' or is_operator(expression[i]):
                    operator_index = i
                    break

        # If still no operator is found, raise an error
        if operator_index == -1:
            raise ValueError("Invalid Expression")

        # Extract the operator and evaluate the operands recursively
        operator = expression[operator_index]
        operand1 = evaluate_helper(start, operator_index - 1)
        operand2 = evaluate_helper(operator_index + 1, end)

        # Perform the operation with the evaluated operands
        return perform_operation(operator, operand1, operand2)

    try:
        # Start the evaluation from the beginning to the end of the expression
        result = evaluate_helper(0, len(expression) - 1)
        return str(result)
    except ValueError as e:
        # Catch and handle any ValueError exceptions, indicating an invalid expression
        return f"Invalid Expression: {e}"

# Test the implementation with example expressions
expression1 = "3 + 12 * 3 / 12"
result1 = evaluate_expression(expression1)
print(f"{expression1} => {result1} valid expression")

expression2 = "(3 + 3) * 42 / (6 + 12)"
result2 = evaluate_expression(expression2)
print(f"{expression2} => {result2}")

expression3 = "4 (12E)"
result3 = evaluate_expression(expression3)
print(f"{expression3} => {result3}")

expression4 = "42+43**271"
result4 = evaluate_expression(expression4)
print(f"{expression4} => {result4}")
