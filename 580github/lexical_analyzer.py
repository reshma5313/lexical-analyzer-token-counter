import re

# C/C++/Java keywords
KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue",
    "default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long", "register",
    "return", "short", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned", "void", "volatile",
    "while", "class", "public", "private", "protected", "new",
    "delete", "try", "catch", "throw", "true", "false"
}

OPERATORS = {
    "==", "!=", "<=", ">=", "++", "--", "+=", "-=", "*=",
    "/=", "%=", "&&", "||", "->", "+", "-", "*", "/", "%",
    "=", "<", ">", "!", "&", "|"
}

SEPARATORS = {
    "(", ")", "{", "}", "[", "]", ";", ",", ":"
}


def lexical_analyzer(source):
    tokens = []

    pattern = re.compile(
        r'//.*|/\*[\s\S]*?\*/'
        r'|"(?:\\.|[^"\\])*"'
        r"|'(?:\\.|[^'\\])*'"
        r'|\d+(?:\.\d+)?'
        r'|[A-Za-z_][A-Za-z0-9_]*'
        r'|==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|%=|&&|\|\||->'
        r'|[+\-*/%=<>!&|]'
        r'|[()[\]{};,:\.]'
    )

    for match in pattern.finditer(source):
        token = match.group()

        # Comments
        if token.startswith("//") or token.startswith("/*"):
            tokens.append((token, "Comment"))

        # String literals
        elif token.startswith('"'):
            tokens.append((token, "String Literal"))

        # Character constants
        elif token.startswith("'"):
            tokens.append((token, "Constant"))

        # Keywords
        elif token in KEYWORDS:
            tokens.append((token, "Keyword"))

        # Identifiers
        elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
            tokens.append((token, "Identifier"))

        # Numeric constants
        elif re.fullmatch(r'\d+(?:\.\d+)?', token):
            tokens.append((token, "Constant"))

        # Operators
        elif token in OPERATORS:
            tokens.append((token, "Operator"))

        # Separators
        elif token in SEPARATORS:
            tokens.append((token, "Separator"))

        # Special symbols
        else:
            tokens.append((token, "Special Symbol"))

    return tokens


def count_tokens(tokens):
    counts = {
        "Keyword": 0,
        "Identifier": 0,
        "Operator": 0,
        "Constant": 0,
        "String Literal": 0,
        "Separator": 0,
        "Special Symbol": 0,
        "Comment": 0
    }

    for _, token_type in tokens:
        counts[token_type] += 1

    return counts


def main():

    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as file:
            source = file.read()

    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    tokens = lexical_analyzer(source)
    counts = count_tokens(tokens)

    # Display output on terminal
    print("\nTOKEN TYPE")
    print("-" * 50)

    for token, token_type in tokens:
        print(f"{token:<25} {token_type}")

    print("\n" + "-" * 50)
    print("TOKEN COUNT")
    print("-" * 50)

    for token_type, count in counts.items():
        print(f"{token_type:<20}: {count}")

    # Save output to output.txt
    with open(output_file, "w") as file:

        file.write("TOKEN TYPE\n")
        file.write("-" * 50 + "\n")

        for token, token_type in tokens:
            file.write(f"{token:<25} {token_type}\n")

        file.write("\n" + "-" * 50 + "\n")
        file.write("TOKEN COUNT\n")
        file.write("-" * 50 + "\n")

        for token_type, count in counts.items():
            file.write(f"{token_type:<20}: {count}")

    print("\nAnalysis completed successfully.")
    print("Output saved to output.txt")


if __name__ == "__main__":
    main()
