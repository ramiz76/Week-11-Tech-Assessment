from main import caclulate_score_for_word, assign_score_to_letter, assign_starting_tiles


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
    result = caclulate_score_for_word(word)
    assert isinstance(result, int)


def test_calculate_score_returns_valid_output():
    word = 'GUARDIAN'
    result = caclulate_score_for_word(word)
    assert result == 10


def test_assign_seven_tiles_with_dist_returns_list():
    result = assign_starting_tiles()
    assert isinstance(result, list)



    
