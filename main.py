def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters = number_of_characters(text)
    book_report(book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    character_dict = {}
    text = text.lower()
    for character in text:
        if character in character_dict:
            character_dict[character] += 1 
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def book_report(path):
    text = get_book_text(path)
    number_of_words = count_words(text)
    character_dict = number_of_characters(text)
    char_list = [{"char": char, "count": count} for char, count in character_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document\n")
    for char_data in char_list:
        if char_data['char'].isalpha():
            print(f"The '{char_data['char']}' character was found {char_data['count']} times")
    print("---End report---")




main()


