import sys
from stats import count_words, count_chars, sort_character_counts


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
           print("Usage: python3 main.py <path_to_book>")
           sys.exit(1)

    book_path = sys.argv[1]

    try:
           text = get_book_text(book_path)
    except FileNotFoundError:
           print(f"Error: The file at '{book_path}' was not found.")
           sys.exit(1)
    except Exception as e:
           print(f"Error: An unexpected error occourred: {e}")
           sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = count_chars(text)
    sorted_char_counts = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


main()
