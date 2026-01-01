from stats import get_book_text, get_num_words, get_num_chars, sort_char_counts

def main():
    book_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f'Analysing book found at the {book_path}...')

    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f'Found {num_words} total words')

    print("--------- Character Count -------")
    char_counts = get_num_chars(text)
    sorted_chars = sort_char_counts(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()
