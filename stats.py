from typing import Dict, List

def get_number_words(text: str) -> None:
    list_of_words = text.split()
    num_words = 0
    for word in list_of_words:
        num_words += 1
    print(f"Found {num_words} total words")


def get_number_of_char_instances(text: str) -> Dict[str, int]:
    instances = {}
    for char in text.lower():
        if char.isalpha():
            if char not in instances:
                instances[char] = 1
            else:
                instances[char] += 1
    return instances

def sort_on(items):
    return items["num"]


def sort_dict(seq: Dict[str, int]) -> List[Dict[str, int]]:
    list_instances = []
    for k, v in seq.items():
        list_instances.append({"char": k, "num": v})
    list_instances.sort(reverse=True, key=sort_on)
    return list_instances