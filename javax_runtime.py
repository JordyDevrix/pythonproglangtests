import errors
import jax_print


def run_javax(ast):
    output_code = True
    global_variables = []

    def run_node(node):

        match node["type"]:
            case "VAR_DECL":
                if node["name"] in [list(variable.keys())[0] for variable in global_variables]:
                    print(errors.variable_already_declared(node["name"]))
                    exit(1)

                match node["value"]["type"]:
                    case "STRING":
                        global_variables.append({node["name"]: str(node["value"]["value"])})
                    case "INT":
                        global_variables.append({node["name"]: int(node["value"]["value"])})
                    case "FLOAT":
                        global_variables.append({node["name"]: float(node["value"]["value"])})
                    case "BOOL":
                        global_variables.append({node["name"]: bool(node["value"]["value"])})
                    case "FUNCTION_CALL":
                        variable = run_node(node["value"])
                        global_variables.append({node["name"]: variable})
                    case "BIN_EXPR":
                        variable = run_node(node["value"])
                        global_variables.append({node["name"]: variable})

            case "FUNCTION_CALL":
                if node["name"] == "print":
                    if output_code:
                        print(jax_print.jax_print(node, global_variables))
                elif node["name"] == "read":
                    arguments = node["arguments"]
                    string = arguments[0]["value"]
                    variable = input(string)
                    return variable

            case "BIN_EXPR":
                if type(node["left"]) == list:
                    left = run_node(node["left"][0])
                else:
                    left = run_node(node["left"])
                if type(node["right"]) == list:
                    right = run_node(node["right"][0])
                else:
                    right = run_node(node["right"])

                match node["operator"]:
                    case "+":
                        return left + right
                    case "-":
                        return left - right
                    case "*":
                        return left * right
                    case "/":
                        return left / right
                    case "%":
                        return left % right
                    case "**":
                        return left ** right

            case "INT":
                return int(node["value"])
            case "FLOAT":
                return float(node["value"])
            case "STRING":
                return str(node["value"])
            case "BOOL":
                return bool(node["value"])

            case "IDENTIFIER":
                for variable in global_variables:
                    if node["value"] == list(variable.keys())[0]:
                        value = list(variable.values())[0]
                        if value.isnumeric():
                            return int(value)
                        elif value.isfloat():
                            return float(value)
                        elif value in ["True", "False"]:
                            return bool(value)
                        else:
                            return value

    for node_data in ast:
        run_node(node_data["NODE"])

