from stats import get_book_text, get_num_words, get_num_chars

def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(text)
    print(f'Found {num_words} total words')
    
    char_count = get_num_chars(text)
    print(char_count)

main()
