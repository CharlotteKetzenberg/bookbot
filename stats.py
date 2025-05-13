def get_book_text(filepath):
    """
    Takes a filepath as input and returns the contents of the file as a string.

    Args:
    filepath(str): Path to the file to be read

    Returns:
    str: Contents of the file as a string
    """
    with open(filepath) as f:
        # Read the entire file contents into a string
        return f.read()

def get_num_words(filepath):
    """
    Takes a filepath as input and returns the number of strings the file has.

    Args:
    filepath(str): Path to the file to be read

    Returns:
    str: Number of words in the file as a string
    """
    with open(filepath) as f:
        strings = f.read().split()

    return len(strings)

def string_to_int(filepath):
    """
    Takes a filepath as input and returns the number of times each character
    appears in the text in a dictionary
    """
    with open(filepath) as f:
        text = f.read()

    string_dictionary = {}
    for char in text:
        if char.isalpha():
            char = char.lower()

            if char in string_dictionary:
                string_dictionary[char] += 1
            else:
                string_dictionary[char] = 1

    # Sort by count (highest to lowest)
    sorted_items = sorted(string_dictionary.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_items