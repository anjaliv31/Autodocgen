import ast

def get_docstring_params(file_path):
    """
    Extract parameter names mentioned in function docstrings.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    functions = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            params = []

            if docstring:
                for line in docstring.splitlines():
                    line = line.strip()

                    # Skip empty lines and headers
                    if not line:
                        continue
                    if line.lower() in ("args:", "arguments:", "parameters:", "returns:"):
                        continue

                    # Extract param name before colon
                    if ":" in line:
                        param = line.split(":", 1)[0]
                        if param.isidentifier():
                            params.append(param)

            functions[node.name] = params

    return functions
