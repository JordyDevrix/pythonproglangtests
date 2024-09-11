
def jax_print(node_content, global_variables):
    arguments = node_content["arguments"][0]
    string = arguments[0]['value']
    local_identifiers = []
    for variable in arguments[1:]:
        for global_variable in global_variables:
            if variable.get("value") == list(global_variable.keys())[0]:
                local_identifiers.append(global_variable)
                break

    lcl_idx = 0
    var_count = 0
    while lcl_idx < len(string):
        if string[lcl_idx:lcl_idx + 2] == "%V":
            insertable = str(list(local_identifiers[var_count].values())[0])
            string = string[:lcl_idx] + insertable + string[lcl_idx + 2:]
            var_count += 1
        lcl_idx += 1

    return string
