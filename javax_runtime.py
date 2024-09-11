import jax_print


def run_javax(ast):
    output_code = True
    global_variables = []
    idx = 0

    def javax():
        nonlocal idx

        while idx < len(ast):
            node_content = ast[idx]["NODE"][0]
            # print(node_content["type"])

            match node_content["type"]:
                case "VAR_DECL":
                    value_name = node_content["name"]
                    value_type = node_content["value"][0]["type"]
                    value = None

                    if value_type == "INT":
                        value = node_content["value"][0].get("value")

                    elif value_type == "FLOAT":
                        value = node_content["value"][0].get("value")

                    elif value_type == "STRING":
                        value = node_content["value"][0].get("value")

                    elif value_type == "BOOL":
                        value = node_content["value"][0].get("value")

                    elif value_type == "FUNCTION_CALL":
                        if node_content["value"][0]["name"] == "read":
                            arguments = node_content["value"][0]["arguments"][0]
                            value = input(arguments[0]["value"])

                    global_variables.append({value_name: value})

                case "FUNCTION_CALL":
                    if node_content["name"] == "print":
                        if output_code:
                            print(jax_print.jax_print(node_content, global_variables))

            idx += 1

    javax()



