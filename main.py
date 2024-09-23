import file_scanner
import javax_runtime
import tokenizer
import parser_example
import parser
import ast_json_maker


def main(debug):
    # Read code from file
    file_path = "code.ys"
    code = file_scanner.read_code(file_path)

    # Tokenize code
    tokens = tokenizer.create_tokens(code)

    # Print tokens
    # for token in tokens:
    #     print(token)

    # Parse tokens and make ast
    # ast = parser_example.parse_tokens(tokens)
    ast = parser.parse_tokens(tokens)

    # Save as json file
    ast_json_maker.save_json(ast, indent=2)

    # Convert ast to json and print ast
    ast_json = ast_json_maker.make_json(ast, indent=2)
    if debug:
        print(ast_json)

    # Run runtime
    javax_runtime.run_javax(ast)


if __name__ == '__main__':
    main(debug=True)
