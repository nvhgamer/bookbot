import sys

from stats import get_word_count, get_count_each_character, get_sorted_char_counts

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path to the book file from command-line arguments
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    
    text = get_book_text(path)
    num_words = get_word_count(text)

    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")

    character_count_dict = get_count_each_character(text)
    sorted_character_count = get_sorted_char_counts(character_count_dict)

    for char_dictionary in sorted_character_count:
        # Skip non-alphabetic characters
        if not char_dictionary['char'].isalpha():
            continue

        print(f"{char_dictionary['char']}: {char_dictionary['num']}")

    print("============= END ===============")

def get_book_text(path_to_file: str) -> str:
    """
    Reads the contents of a text file and returns it as a string.

    Args:
        path_to_file (str): The path to the file to be read.

    Returns:
        str: The entire contents of the file as a single string.
    """

    with open(path_to_file) as f:
        # read all the text and return it as a string
        return f.read()
    
if __name__ == "__main__":
    main()