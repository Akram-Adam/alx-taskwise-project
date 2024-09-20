"""
	Module for extra function to handle the input or
	other extra functions
"""

def is_list_part_of(A_list, B_list):
    """
    Fucntion check if the function is part of anther function
    :param A_list: list of element
    :param B_list: list of element
    """
    for i in A_list:
        if i not in B_list:
            return False
    return True


def get_Config_data(path):
    """ functhon that Read config file and return dict """
    Config_data_return = dict()

    try:
        with open(path, 'r') as Config_data:
            data = Config_data.read()
            data = data.split('\n')

            for line in data:
                if line and not line.startswith('/'):
                    try:
                        key, value = line.split('=', 1)  # Split on the first '=' to handle cases where value contains '='
                        Config_data_return[key.strip()] = value.strip()  # Remove leading/trailing whitespace
                    except ValueError:
                        print(f"Skipping malformed line: {line}")

    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to open '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return Config_data_return

