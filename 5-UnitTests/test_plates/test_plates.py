from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50")
    assert is_valid("AB1234")
    assert is_valid("ABCDEF")


def test_length_rules():
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")


def test_first_two_must_be_letters():
    assert not is_valid("1ABC")
    assert not is_valid("A1BC")


def test_no_punctuation_or_spaces():
    assert not is_valid("AB.12")
    assert not is_valid("AB 12")


def test_first_number_cannot_be_zero():
    assert not is_valid("AA012")


def test_no_letters_after_numbers_start():
    assert not is_valid("AA1A")
