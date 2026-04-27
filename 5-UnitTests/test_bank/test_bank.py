from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("    hello") == 0


def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("hey") == 20


def test_not_h():
    assert value("goodmorning") == 100
