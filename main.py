def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_character_count(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in char_count:
        print(f"The '{item['char']}' character was found '{item['num']}' times")

def sort_on(dict):
    return dict["num"]


def get_character_count(text):
    lowered_text = text.lower()
    chars = {}
    for char in lowered_text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    
    dict_list = []
    for char in chars:
        count = chars[char]
        dict_list.append({"char": char, "num": count})
    
    dict_list.sort(key=sort_on, reverse=True)

    return dict_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()