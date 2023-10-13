path = "books/frankenstein.txt"

def main():
    with open(path) as f:
        file_contents = f.read()
    num_word = word_count(file_contents)
    # print(f"words in the file is {num_word}")

    num_char = char_count(file_contents)
    # print(f'char in the file is\n{num_char}')

    print_report(num_char, num_word)


def word_count(str):
    words = str.split()
    return len(words)

def char_count(str):
    char = {}
    for c in str:
        small_c = c.lower()
        if small_c in char:
            char[small_c] += 1
        else:
            char[small_c] = 1
    return char

def print_report(some_dict, num_word):
    some_list = []
    for key in some_dict:
        if key.isalpha():
            some_list.append(key)
    some_list.sort()

    print(f'---------------BEGIN TO REPORT OF {path}---------------')
    print(f'{num_word} words was found in the document\n')
    for char in some_list:
        print(f'The {char} character was found {some_dict[char]} times')
    print(f'---------------END OF REPORT---------------')

main()

# some_dict = {
#     'a': 1,
#     'z': 90,
#     'd': 87,
#     't': 12
# }

# some_list = list(some_dict)
# print(some_list)

# for i in some_dict:
#     print(i)