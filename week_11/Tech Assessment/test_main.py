from main import calculate_score_for_word, assign_score_to_letter, assign_starting_tiles, check_letter_count, create_alphabet, assign_starting_tiles_with_distribution, random_generator


def test_assign_score_returns_int():
    letter = 'A'
    result = assign_score_to_letter('A')
    assert isinstance(result, int)


def test_assign_score_when_letter_is_A():
    letter = 'A'
    result = assign_score_to_letter(letter)
    assert result == 1


def test_assign_score_when_letter_is_G():
    letter = 'G'
    result = assign_score_to_letter(letter)
    assert result == 2


def test_calculate_score_returns_int():
    word = 'GUARDIAN'
    result = calculate_score_for_word(word)
    assert isinstance(result, int)


def test_calculate_score_returns_valid_output():
    word = 'GUARDIAN'
    result = calculate_score_for_word(word)
    assert result == 10


def test_assign_seven_tiles_with_dist_returns_list():
    result = assign_starting_tiles()
    assert isinstance(result, list)


def test_letter_count_returns_bool():
    alphabet = create_alphabet()
    result = check_letter_count(alphabet, 'A')
    assert isinstance(result, int)


def test_letter_count_if_letter_is_A():
    alphabet = create_alphabet()
    result = check_letter_count(alphabet, 'A')
    assert result == True


def test_assign_starting_with_dist_returns_list():
    result = assign_starting_tiles_with_distribution()
    assert isinstance(result, list)

