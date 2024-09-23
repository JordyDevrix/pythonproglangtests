import errors
import jax_print


def run_javax(ast):
    output_code = True
    global_variables = []

    def run_node(node):

        match node["type"]:
            case "VAR_DECL":
                for index in range(len(global_variables)):
                    if node["name"] == list(global_variables[index].keys())[0]:
                        global_variables.pop(index)
                        break
                match node["value"]["type"]:

                    case "STRING":
                        global_variables.append({node["name"]: str(node["value"]["value"])})
                    case "INT":
                        global_variables.append({node["name"]: int(node["value"]["value"])})
                    case "FLOAT":
                        global_variables.append({node["name"]: float(node["value"]["value"])})
                    case "BOOL":
                        if node["value"]["value"] == "True":
                            global_variables.append({node["name"]: True})
                        elif node["value"]["value"] == "False":
                            global_variables.append({node["name"]: False})
                    case "FUNCTION_CALL":
                        variable = run_node(node["value"])
                        global_variables.append({node["name"]: variable})
                    case "BIN_EXPR":
                        variable = run_node(node["value"])
                        global_variables.append({node["name"]: variable})
                    case "IDENTIFIER":
                        for variable in global_variables:
                            if node["value"]["value"] == list(variable.keys())[0]:
                                value = run_node(node["value"])
                                global_variables.append({node["name"]: value})
                                break

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
                if node["value"] == "True":
                    return True
                elif node["value"] == "False":
                    return False

            case "IDENTIFIER":
                for variable in global_variables:
                    if node["value"] == list(variable.keys())[0]:
                        value = list(variable.values())[0]
                        if isinstance(value, int):
                            return int(value)
                        elif isinstance(value, float):
                            return float(value)
                        elif isinstance(value, bool):
                            return bool(value)
                        else:
                            return value

            case "IF_STATEMENT":
                condition = run_node(node["condition"])
                if condition:
                    for child in node["child"]:
                        run_node(child)

    for node_data in ast:
        run_node(node_data["NODE"])

