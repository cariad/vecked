from typing import Any

from pytest import mark, raises

from vecked import Vector2f, Vector2i


@mark.parametrize(
    "vector, expect",
    [
        (
            Vector2i(2, 3),
            Vector2i(2, 3),
        ),
        (
            Vector2i(-2, 3),
            Vector2i(2, 3),
        ),
        (
            Vector2i(2, -3),
            Vector2i(2, 3),
        ),
        (
            Vector2i(-2, -3),
            Vector2i(2, 3),
        ),
    ],
)
def test_abs(
    vector: Vector2i,
    expect: Vector2i,
) -> None:
    assert abs(vector) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Vector2i(2, 3),
            Vector2i(7, 12),
            Vector2i(9, 15),
        ),
        (
            Vector2i(2, 3),
            Vector2f(0.25, 0.75),
            Vector2f(2.25, 3.75),
        ),
    ],
)
def test_add(
    a: Vector2i,
    b: Vector2f | Vector2i,
    expect: Vector2f | Vector2i,
) -> None:
    assert a + b == expect


@mark.parametrize(
    "other, expect",
    [
        (None, "cannot add None to Vector2i(0, 0)"),
        ("pizza", "cannot add 'pizza' to Vector2i(0, 0)"),
    ],
)
def test_add__invalid(other: object, expect: str) -> None:
    with raises(ValueError) as ex:
        _ = Vector2i(0, 0) + other  # type: ignore

    assert str(ex.value) == expect


@mark.parametrize(
    "vector, other, expect",
    [
        (Vector2i(0, 0), None, False),
        (Vector2i(0, 0), Vector2i(0, 1), False),
        (Vector2i(0, 0), Vector2i(0, 0), True),
        (Vector2i(0, 0), (0, 1), False),
        (Vector2i(0, 0), (0, 0), True),
        (Vector2i(0, 0), "pizza", False),
    ],
)
def test_eq(
    vector: Vector2i,
    other: Any,
    expect: bool,
) -> None:
    assert (vector == other) is expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Vector2i(3, 9),
            -1,
            Vector2i(-3, -9),
        ),
        (
            Vector2i(3, 9),
            -1.5,
            Vector2f(-4.5, -13.5),
        ),
        (
            Vector2i(3, 9),
            Vector2i(2, 3),
            Vector2i(6, 27),
        ),
        (
            Vector2i(3, 9),
            Vector2f(1.5, 2.5),
            Vector2f(4.5, 22.5),
        ),
    ],
)
def test_mul(
    a: Vector2i,
    b: float | int | Vector2f | Vector2i,
    expect: Vector2f | Vector2i,
) -> None:
    result = a * b
    assert result == expect


@mark.parametrize(
    "other, expect",
    [
        (None, "cannot multiply Vector2i(0, 0) by None"),
        ("pizza", "cannot multiply Vector2i(0, 0) by 'pizza'"),
    ],
)
def test_mul__invalid(other: object, expect: str) -> None:
    with raises(ValueError) as ex:
        _ = Vector2i(0, 0) * other  # type: ignore

    assert str(ex.value) == expect


def test_repr() -> None:
    assert repr(Vector2i(3, 9)) == "Vector2i(3, 9)"


def test_str() -> None:
    assert str(Vector2i(3, 9)) == "(3, 9)"


@mark.parametrize(
    "a, b, expect",
    [
        (
            Vector2i(9, 15),
            Vector2i(2, 3),
            Vector2i(7, 12),
        ),
        (
            Vector2i(2, 3),
            Vector2f(0.25, 0.75),
            Vector2f(1.75, 2.25),
        ),
    ],
)
def test_sub(
    a: Vector2i,
    b: Vector2f | Vector2i,
    expect: Vector2f | Vector2i,
) -> None:
    result = a - b
    assert result == expect


@mark.parametrize(
    "other, expect",
    [
        (None, "cannot subtract None from Vector2i(0, 0)"),
        ("pizza", "cannot subtract 'pizza' from Vector2i(0, 0)"),
    ],
)
def test_sub__invalid(other: object, expect: str) -> None:
    with raises(ValueError) as ex:
        _ = Vector2i(0, 0) - other  # type: ignore

    assert str(ex.value) == expect


def test_vector() -> None:
    assert Vector2i(3, 9).vector == (3, 9)


def test_x() -> None:
    assert Vector2i(3, 9).x == 3


def test_y() -> None:
    assert Vector2i(3, 9).y == 9
