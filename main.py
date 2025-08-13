import sys
from stats import count_words, count_characters, sorted_list

def get_book_text(file_path) -> str:
    with open(file_path,"r") as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    count_word = count_words(get_book_text(file_path))
    count_character = count_characters(get_book_text(file_path))
    sorted_l = sorted_list(count_character)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {(file_path)}...")
    print("----------- Word Count ----------")
    print(f"{count_word}")
    print("--------- Character Count -------")

    for item in sorted_l:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
    
if __name__ == "__main__":
    main()