from ast import literal_eval


def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


def les_types(valeurrecherchee):
    print(get_type(valeurrecherchee))
