import javax_tokens


def parse_tokens(tokens):
    idx = 0
    ast = []

    def parse_expression():
        nonlocal idx
        expression = []

        while idx < len(tokens):
            token_type = tokens[idx][0]
            token_value = tokens[idx][1]

            if (token_type == "KEYWORD") and (token_value in javax_tokens.keywords):
                function_name = token_value
                idx += 2
                arguments = []  # making a list of arguments to pass to the function
                while tokens[idx] != ("SYMBOL", ")"):
                    arguments.append(parse_expression())
                idx += 1    # This is to skip the closing bracket
                expression.append(
                    {
                        "type": "FUNCTION_CALL",
                        "name": function_name,
                        "arguments": arguments
                    }
                )

            elif token_type in javax_tokens.variables:
                expression.append({"type": token_type, "value": token_value})
                idx += 1
            elif token_type == "IDENTIFIER":
                if (idx + 1 < len(tokens)) and (tokens[idx + 1] == ("ASSIGN", "=")):
                    idx += 2    # Skip the assignment operator
                    expression.append(
                        {
                            "type": "VAR_DECL",
                            "name": token_value,
                            "value": parse_expression()
                        }
                    )
                else:
                    print(f"{tokens[idx]} - correct")
                    expression.append({"type": token_type, "value": token_value})
                    idx += 1    # IMPORTANT TO BREAK THE LOOP
            elif token_type == "OPERATOR":
                idx += 1
                expression = {
                    "type": "BIN_EXPR",
                    "operator": token_value,
                    "left": expression,
                    "right": parse_expression()
                }
            elif token_type == "IFSTATE":
                print(tokens[idx])
                idx += 2    # Skip the opening bracket
                print(tokens[idx])
                node_exp = {
                    "type": "IF_STATEMENT",
                    "condition": parse_expression(),
                    "child": None
                }
                print(tokens[idx])
                idx += 1
                print(f"{tokens[idx]} - after")
                node_exp["child"] = parse_expression()
                expression.append(node_exp)
                idx += 1

            elif (token_type == "SYMBOL") and (token_value in (")", ";")):
                break
            elif (token_type == "SYMBOL") and (token_value in ("(", "{")):
                idx += 1
                expression = parse_expression()
                idx += 1
            else:
                idx += 1

        return expression[0] if len(expression) == 1 else expression

    while idx < len(tokens):
        node = {"NODE": parse_expression()}
        # Check if node is not empty and append to ast list
        if node:
            ast.append(node)

        if idx < len(tokens) and tokens[idx] == ("SYMBOL", ";"):
            idx += 1

    return ast
