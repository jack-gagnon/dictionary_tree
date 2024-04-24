def print_dict_structure(dictionary, indent=0):
    for key, value in dictionary.items():
        print("  " * indent + str(key))
        
        if isinstance(value, dict):
            print_dict_structure(value, indent + 1)  # Recursive call
        elif isinstance(value, pd.DataFrame):  # Custom handling for DataFrames
            print("  " * (indent + 1) + "DataFrame with {} rows and {} columns".format(value.shape[0], value.shape[1]))
        elif isinstance(value, list):
            print("  " * (indent + 1) + "List with {} items".format(len(value)))
        else:
            print("  " * (indent + 1) + str(type(value).__name__))

# Example usage:
dict1 = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        }
    },
    'g': 5
}

dict2 = {
    'e': 1
}

print_dict_structure(dict1)
print_dict_structure(dict2)
