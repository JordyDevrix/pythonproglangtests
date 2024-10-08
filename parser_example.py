import json

import tokenizer


def parse_tokens(tokens):
    index = 0
    ast = []

    def parse_expression():
        nonlocal index
        expression = []

        while index < len(tokens):
            token_type, token_value = tokens[index]

            if token_type == 'KEYWORD' and token_value in ('print', 'read'):
                # Parse function call
                func_name = token_value
                index += 2  # Skip '('
                args = []
                while tokens[index] != ('SYMBOL', ')'):
                    args.append(parse_expression())
                    # if tokens[index] == ('SYMBOL', ','):
                    #     index += 1  # Skip ','
                index += 1  # Skip ')'
                expression.append({
                    "type": "FunctionCall",
                    "name": func_name,
                    "arguments": args
                })

            elif token_type in ('INT', 'FLOAT', 'STRING', 'BOOL'):
                # Parse literals
                expression.append({
                    "type": token_type,
                    "value": token_value
                })
                index += 1
            elif token_type == 'IDENTIFIER':
                # Parse variable or assignment
                ident = token_value
                if index + 1 < len(tokens) and tokens[index + 1] == ('ASSIGN', '='):
                    index += 2  # Skip '='
                    value = parse_expression()
                    expression.append({
                        "type": "VariableDeclaration",
                        "name": ident,
                        "value": value
                    })
                else:
                    expression.append({
                        "type": "Identifier",
                        "name": ident
                    })
                    index += 1
            elif token_type == 'OPERATOR':
                # Parse operators
                operator = token_value
                index += 1
                right = parse_expression()
                expression = {
                    "type": "BinaryExpression",
                    "operator": operator,
                    "left": expression,
                    "right": right
                }
            elif token_type == 'SYMBOL' and token_value in (';', ')', '}'):
                break
            elif token_type == 'SYMBOL' and token_value in ('(', '{'):
                index += 1
                expression = parse_expression()
                index += 1  # Skip ')'
            else:
                index += 1

            print(index, len(tokens))
        return expression[0] if len(expression) == 1 else expression

    while index < len(tokens):
        node = parse_expression()
        # Append node to ast
        if node:
            print(node)
            ast.append(node)

        # Skip semicolon
        if index < len(tokens) and tokens[index] == ('SYMBOL', ';'):
            index += 1

    ast_final = ast
    return ast_final


# Example usage with your token list:

