import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as f:
        book_text = f.read()
    return book_text

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_list = count_characters(book_text)
    sorting = sort_list(char_list)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path +"...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorting:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

        
 
    
    
from stats import count_words, count_characters, sort_list
# from stats import

main()
