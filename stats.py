def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(item):
    return item["num"]

def sort_char_counts(char_counts):
    result = []

    for char in char_counts:
        if char.isalpha():
            result.append({
                "char": char,
                "num": char_counts[char]
            })
    result.sort(reverse=True, key=sort_on)
    return result
