from parser.code_parser import get_functions_and_params
from parser.docstring_parser import get_docstring_params

FILE_PATH = "examples/sample.py"

code_params = get_functions_and_params(FILE_PATH)
doc_params = get_docstring_params(FILE_PATH)

for func in code_params:
    code_set = set(code_params.get(func, []))
    doc_set = set(doc_params.get(func, []))

    missing_in_docs = code_set - doc_set
    extra_in_docs = doc_set - code_set

    for param in missing_in_docs:
        print(f"⚠️ {func}(): parameter '{param}' missing in documentation")

    for param in extra_in_docs:
        print(f"⚠️ {func}(): parameter '{param}' documented but not in code")
