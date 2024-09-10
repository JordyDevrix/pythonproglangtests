import file_scanner
import tokenizer
import parser_example
import parser
import ast_json_maker


def main():
    # Read code from file
    file_path = "code2.txt"
    file_scanner.read_code(file_path)

    # Tokenize code
    tokens = tokenizer.create_tokens()

    # Print tokens
    print(tokens)

    # Parse tokens and make ast
    ast = parser_example.parse_tokens(tokens)

    # Covert ast to json and save as json file
    ast = ast_json_maker.make_json(ast, indent=2)
    ast_json_maker.save_json(ast, indent=2)

    # Print ast
    print(ast)


if __name__ == '__main__':
    main()
