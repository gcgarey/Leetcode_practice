
def evaluate_reverse(tokens):
    stack = []
    operators = "+-*/"
    for token in tokens:
        if token in operators:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num2 - num1)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                stack.append(num2 / num1)
        else:
            stack.append(token)

    return int(stack[-1])