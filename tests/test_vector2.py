from vecked import Vector2


def test_x() -> None:
    assert Vector2(3, 9).x == 3


def test_y() -> None:
    assert Vector2(3, 9).y == 9
