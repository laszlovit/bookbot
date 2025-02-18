def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = 0
    words = file_contents.split()

    for word in words:
        word_count += 1

    def count_characters():
        character_dict = {}
        lower_cased_file_content = file_contents.lower()

        for character in lower_cased_file_content:
            if character in character_dict:
                character_dict[character] += 1
            else: character_dict[character] = 1
        
        return character_dict
    
    def print_report():
        counted_characters = count_characters()
        characters_list = []

        for i in counted_characters:
            characters = {
            "letter": i,
            "count": counted_characters[i]
            }
            if i.isalpha() == True:
                characters_list.append(characters)

        for item in characters_list:
            print(f"The '{item["letter"]}' character was found {item["count"]} times")
    

    print_report()

main()