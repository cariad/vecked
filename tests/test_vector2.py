from typing import Any

from pytest import mark

from vecked import AnyNumber, TVector, Vector2


@mark.parametrize(
    "a, b, expect",
    [
        (Vector2(0, 0), Vector2(2, 3), Vector2(2, 3)),
        (Vector2(7, 9), (-10, -10), Vector2(17, 19)),
    ],
)
def test_distance_to(
    a: Vector2[AnyNumber],
    b: Vector2[AnyNumber] | TVector[AnyNumber],
    expect: Vector2[AnyNumber],
) -> None:
    assert a.distance_to(b) == expect


@mark.parametrize(
    "vector, other, expect",
    [
        (Vector2(0, 0), None, False),
        (Vector2(0, 0), Vector2(0, 1), False),
        (Vector2(0, 0), Vector2(0, 0), True),
        (Vector2(0, 0), (0, 1), False),
        (Vector2(0, 0), (0, 0), True),
        (Vector2(0, 0), "pizza", False),
    ],
)
def test_eq(
    vector: Vector2[AnyNumber],
    other: Any,
    expect: bool,
) -> None:
    assert (vector == other) is expect


def test_str() -> None:
    assert str(Vector2(3, 9)) == "(3, 9)"


def test_vector() -> None:
    assert Vector2(3, 9).vector == (3, 9)


def test_x() -> None:
    assert Vector2(3, 9).x == 3


def test_y() -> None:
    assert Vector2(3, 9).y == 9
