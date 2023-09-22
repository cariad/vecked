from pytest import mark, raises

from vecked import Vector2f, Vector2i


@mark.parametrize(
    "vector, expect",
    [
        (
            Vector2f(2.2, 3.3),
            Vector2f(2.2, 3.3),
        ),
        (
            Vector2f(-2.2, 3.3),
            Vector2f(2.2, 3.3),
        ),
        (
            Vector2f(2.2, -3.3),
            Vector2f(2.2, 3.3),
        ),
        (
            Vector2f(-2.2, -3.3),
            Vector2f(2.2, 3.3),
        ),
    ],
)
def test_abs(
    vector: Vector2f,
    expect: Vector2f,
) -> None:
    assert abs(vector) == expect


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
    "vector, a, b, expect",
    [
        (
            Vector2f(1, 1),
            Vector2f(0, 0),
            Vector2f(2, 2),
            Vector2f(0.5, 0.5),
        ),
        (
            Vector2f(0, 0),
            Vector2f(0, 0),
            Vector2f(2, 2),
            Vector2f(0, 0),
        ),
        (
            Vector2f(-1, 4),
            Vector2f(0, 0),
            Vector2f(2, 2),
            Vector2f(-0.5, 2),
        ),
    ],
)
def test_inverse_lerp(
    vector: Vector2f,
    a: Vector2f,
    b: Vector2f,
    expect: Vector2f,
) -> None:
    assert vector.inverse_lerp(a, b) == expect


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
    "vector, origin, expect",
    [
        (
            Vector2f(0, 0),
            Vector2f(0, 0),
            Vector2f(0, 0),
        ),
        (
            Vector2f(-1, -1),
            Vector2f(0, 0),
            Vector2f(1, 1),
        ),
        (
            Vector2f(-4, 3),
            Vector2f(1, 2),
            Vector2f(6, 1),
        ),
    ],
)
def test_reflect_across(
    vector: Vector2f,
    origin: Vector2f,
    expect: Vector2f,
) -> None:
    result = vector.reflect_across(origin)
    assert result == expect


@mark.parametrize(
    "vector, x, expect",
    [
        (Vector2f(0, 0), 0, Vector2f(0, 0)),
        (Vector2f(0, 0), 1, Vector2f(2, 0)),
        (Vector2f(-2, 0), 1, Vector2f(4, 0)),
        (Vector2f(4, 0), 1, Vector2f(-2, 0)),
        (Vector2f(2.5, 0), 3.5, Vector2f(4.5, 0)),
    ],
)
def test_reflect_horizontally(
    vector: Vector2f,
    x: float,
    expect: Vector2f,
) -> None:
    result = vector.reflect_horizontally(x)
    assert result == expect


@mark.parametrize(
    "vector, y, expect",
    [
        (Vector2f(0, 0), 0, Vector2f(0, 0)),
        (Vector2f(0, 0), 1, Vector2f(0, 2)),
        (Vector2f(0, -2), 1, Vector2f(0, 4)),
        (Vector2f(0, 4), 1, Vector2f(0, -2)),
        (Vector2f(0, 2.5), 3.5, Vector2f(0, 4.5)),
    ],
)
def test_reflect_vertically(
    vector: Vector2f,
    y: float,
    expect: Vector2f,
) -> None:
    result = vector.reflect_vertically(y)
    assert result == expect


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
