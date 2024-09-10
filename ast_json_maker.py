import json


def make_json(ast, indent=2):
    ast_json = json.dumps(ast, indent=indent)
    return ast_json


def save_json(ast, indent=2) -> None:
    ast_json = json.dumps(ast, indent=indent)

    with open("ast.json", "w") as f:
        f.write(ast_json)
    return None
