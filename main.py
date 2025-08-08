import sys

from stats import get_word_count
from stats import get_char_count
from stats import sort_list

file_contents = ""
word_count = 0
char_dict = {}
sorted_list = []
if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()  
    return file_contents

def main():
    file_contents = get_book_text(filepath)
    word_count = get_word_count(file_contents)
    char_dict = get_char_count(file_contents)
    #print(char_dict)
    sorted_list = sort_list(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + filepath + "...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print("{}: {}".format(item["char"],item["num"]))
        else:
            pass
    print("============= END ===============")
main()