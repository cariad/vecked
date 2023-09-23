from pytest import mark

from vecked import Region2f, Vector2f


@mark.parametrize(
    "vector, expect",
    [
        (Vector2f(2, 2), Vector2f(3, 3)),
        (Vector2f(3, 3), Vector2f(4.75, 5)),
        (Vector2f(4, 4), Vector2f(6.5, 7)),
        (Vector2f(5, 5), Vector2f(8.25, 9)),
        (Vector2f(6, 6), Vector2f(10, 11)),
    ],
)
def test_interpolate(vector: Vector2f, expect: Vector2f) -> None:
    region = Region2f(
        Vector2f(2, 2),
        Vector2f(4, 4),
    )

    into = Region2f(
        Vector2f(3, 3),
        Vector2f(7, 8),
    )

    result = region.interpolate(
        vector,
        into,
    )

    assert result == expect


def test_str() -> None:
    region = Region2f(
        Vector2f(1, 2),
        Vector2f(3, 4),
    )

    assert str(region) == "(1, 2)x(3, 4)"
