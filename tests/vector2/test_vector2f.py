from pytest import mark, raises

from vecked import Vector2f, Vector2i


@mark.parametrize(
    "a, b, expect",
    [
        (
            Vector2f(2.25, 3.75),
            Vector2i(7, 12),
            Vector2f(9.25, 15.75),
        ),
        (
            Vector2f(2.25, 3.75),
            Vector2f(0.25, 0.75),
            Vector2f(2.5, 4.5),
        ),
    ],
)
def test_add(
    a: Vector2f,
    b: Vector2f | Vector2i | tuple[float, float] | tuple[int, int],
    expect: Vector2f,
) -> None:
    assert a + b == expect


@mark.parametrize(
    "other, expect",
    [
        (None, "cannot add None to Vector2f(0, 0)"),
        ("pizza", "cannot add 'pizza' to Vector2f(0, 0)"),
    ],
)
def test_add__invalid(other: object, expect: str) -> None:
    with raises(ValueError) as ex:
        _ = Vector2f(0, 0) + other

    assert str(ex.value) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Vector2f(2.25, 3.75),
            2,
            Vector2f(4.5, 7.5),
        ),
        (
            Vector2f(2.25, 3.75),
            Vector2f(4, 8),
            Vector2f(9, 30),
        ),
    ],
)
def test_mul(
    a: Vector2f,
    b: float | Vector2f,
    expect: Vector2f,
) -> None:
    result = a * b
    assert result == expect


@mark.parametrize(
    "other, expect",
    [
        (None, "cannot multiply Vector2f(0, 0) by None"),
        ("pizza", "cannot multiply Vector2f(0, 0) by 'pizza'"),
    ],
)
def test_mul__invalid(other: object, expect: str) -> None:
    with raises(ValueError) as ex:
        _ = Vector2f(0, 0) * other

    assert str(ex.value) == expect


@mark.parametrize(
    "a, b, expect",
    [
        (
            Vector2f(9.25, 15.75),
            Vector2i(2, 3),
            Vector2f(7.25, 12.75),
        ),
        (
            Vector2f(2.5, 4.5),
            Vector2f(0.25, 0.75),
            Vector2f(2.25, 3.75),
        ),
    ],
)
def test_sub(
    a: Vector2f,
    b: Vector2f | Vector2i,
    expect: Vector2f,
) -> None:
    result = a - b
    assert result == expect


@mark.parametrize(
    "other, expect",
    [
        (None, "cannot subtract None from Vector2f(0, 0)"),
        ("pizza", "cannot subtract 'pizza' from Vector2f(0, 0)"),
    ],
)
def test_sub__invalid(other: object, expect: str) -> None:
    with raises(ValueError) as ex:
        _ = Vector2f(0, 0) - other

    assert str(ex.value) == expect
