from stats import get_number_words, get_number_of_char_instances, sort_dict
import sys

def get_book_text(file: str) -> str:
    with open(file) as f:
        return f.read()




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    file = str(sys.argv[1])
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    text_str = get_book_text(file)
    get_number_words(text_str)
    instances = sort_dict(get_number_of_char_instances(text_str))
    print("--------- Character Count -------")
    for pair in instances:
        k, v = pair["char"], pair["num"]
        print(f"{k}: {v}")
    print("============= END ===============")


if __name__ == "__main__":
    main()

