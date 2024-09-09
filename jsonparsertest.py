def json_to_ast(json_data):
    """
    Converts a JSON object into an AST representation.
    """
    if isinstance(json_data, dict):
        return {
            "type": "Object",
            "children": [
                {
                    "type": "KeyValuePair",
                    "key": key,
                    "value": json_to_ast(value)
                }
                for key, value in json_data.items()
            ]
        }
    elif isinstance(json_data, list):
        return {
            "type": "Array",
            "children": [json_to_ast(item) for item in json_data]
        }
    elif isinstance(json_data, str):
        return {
            "type": "String",
            "value": json_data
        }
    elif isinstance(json_data, (int, float)):
        return {
            "type": "Number",
            "value": json_data
        }
    elif isinstance(json_data, bool):
        return {
            "type": "Boolean",
            "value": json_data
        }
    elif json_data is None:
        return {
            "type": "Null"
        }
    else:
        raise TypeError(f"Unsupported data type: {type(json_data)}")


def print_ast(ast, indent=0):
    """
    Recursively prints the AST in a readable format.
    """
    space = ' ' * indent
    if "value" in ast:
        print(f"{space}{ast['type']}: {ast['value']}")
    else:
        print(f"{space}{ast['type']}")
        if "children" in ast:
            for child in ast["children"]:
                print_ast(child, indent + 2)


# Example usage
json_data = {
    "name": "ChatGPT",
    "age": 2,
    "features": ["NLP", "AI"],
    "active": True,
    "score": None
}

# Generate the AST
ast = json_to_ast(json_data)

# Print the AST
print_ast(ast)
