from stats import get_num_words, get_num_char, get_sort_dict
import sys

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        fullbook = get_book_test(filepath)
        num_words = get_num_words(fullbook)
        num_char = get_num_char(fullbook)
        list_char = get_sort_dict(num_char)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at { filepath }...")
        print("----------- Word Count ----------")
        print(f"Found { num_words } total words")
        print("--------- Character Count -------")
        for k in list_char:
            if k["char"].isalpha():
                print(f"{ k['char'] }: { k['num'] }")
        print("============= END ===============")


if __name__ == "__main__":
     main()