import random
import string


def assign_score_to_letter(letter) -> int:
    alphabet = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2,
                "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1,
                "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1,
                "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}
    return alphabet[letter]


def calculate_score_for_word(word: str) -> int:
    points = 0
    for letter in word:
        letter = letter.upper()
        points += assign_score_to_letter(letter)
    return points


def assign_starting_tiles() -> list:
    """Player starts with 7 tiles and this function assigns 7 random tiles to them"""
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    player_hand = []
    for i in range(7):
        alpha_index = random.randint(0, 25)
        player_hand.append(alphabet[alpha_index])
    return player_hand


def random_generator():
    random_letter = random.choice(string.ascii_letters).upper()
    return random_letter


def assign_starting_tiles_with_distribution() -> list:
    """Player starts with 7 tiles and this function assigns 7 random tiles to them based on distribution"""
    alphabet = create_alphabet()
    player_hand = []
    for i in range(7):
        valid = False
        while valid == False:
            random_letter = random_generator()
            if check_letter_count(alphabet, random_letter):
                alphabet[random_letter] = alphabet[random_letter]-1
                player_hand.append(random_letter)
                valid = True
    return player_hand


def check_letter_count(alphabet, random_letter) -> bool:
    if alphabet[random_letter] > 0:
        return True
    return False


def create_alphabet():
    alphabet = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3,
                "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6,
                "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4,
                "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}
    return alphabet


def read_dict_file():
    with open('dictionary.txt', 'r') as f:
        return f.readlines()


# def find_valid_words(dictionary: list[str], tiles: list) -> list:
#     valid_words = []
#     word = "".join(tiles)
#     for valid in dictionary:
#         checking_valid = valid.upper().strip()
#         checking_valid = sorted(checking_valid)

#         if checking_valid == sorted(tiles[0]) or checking_valid == sorted(tiles[:2]) or checking_valid == sorted(tiles[:3]):
#             valid_words.append(valid.strip())
#         if checking_valid == sorted(tiles[:4]) or checking_valid == sorted(tiles[:5]) or checking_valid == sorted(tiles[:6]) or checking_valid == sorted(tiles):
#             valid_words.append(valid.strip())
#     return valid_words


def find_valid_words(dictionary: list[str], tiles: list) -> list:
    valid_words = []
    word = "".join(tiles)
    for valid in dictionary:
        checking_valid = valid.upper().strip()
        checking_valid = sorted(checking_valid)
        for i in range(1, 8):
            if checking_valid == sorted(tiles[:i]):
                valid_words.append(valid.strip())

    return valid_words


def find_longest_valid_word(valid_words):
    longest = ""
    for word in valid_words:
        if len(word) > len(longest):
            longest = word
    return longest


def find_highest_scoring_word(valid_words):
    highest_word = ""
    highest_score = 0
    for word in valid_words:
        if word:
            score = calculate_score_for_word(word)
            if score > highest_score:
                highest_score = score
                highest_word = word
    return highest_word


if __name__ == "__main__":
    dictionary = read_dict_file()
    starting_tiles = assign_starting_tiles_with_distribution()
    print(starting_tiles)
    valid_words = find_valid_words(dictionary, starting_tiles)
    if valid_words:
        print(f'All available words: {valid_words}')
        print(f'Longest word: {find_longest_valid_word(valid_words)}')
        print(f'Best word: {find_highest_scoring_word(valid_words)}')

    else:
        print("No words to create!")
