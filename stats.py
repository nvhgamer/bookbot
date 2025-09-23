def get_word_count(text: str) -> int:
    """
    Counts the number of words in a given text string.

    Args:
        text (str): The input text string.
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_count_each_character(text: str) -> dict[str, int]:
    """
    Counts the occurrences of each character in the given text (case insensitive).

    Args:
        text (str): The input text string.

    Returns:
        dict: A dictionary where keys are characters and values are their counts.
    """
    # Convert the text to lowercase to ensure case insensitivity of character counts
    lowercase_text = text.lower()
    
    # Initialize an empty dictionary to hold character counts
    char_counts = {}

    # Iterate through each character in the text
    for char in lowercase_text:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_counts[char] = 1

    return char_counts

def get_sorted_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    """
    Converts a character count dictionary to a sorted list of dictionaries.
    Each dictionary has keys 'char' and 'num', sorted by 'num' descending.

    Args:
        char_counts (dict): Dictionary of character counts.

    Returns:
        list: List of dictionaries sorted by count descending.
        Each dictionary is of the form `{"char": character, "num": count}`.
    """
    char_list = []

    # Convert the character count dictionary to a list of dictionaries ready for sorting
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    # Sort the list of dictionaries by the 'num' key in descending order
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
    

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]
