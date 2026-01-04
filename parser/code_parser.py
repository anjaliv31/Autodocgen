import ast

def get_functions_and_params(file_path):
    """
    Extract function names and parameters from Python code.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    functions = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            params = [arg.arg for arg in node.args.args]
            functions[node.name] = params

    return functions
