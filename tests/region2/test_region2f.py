from pytest import mark

from vecked import Region2f, Vector2f


@mark.parametrize(
    "point, expect",
    [
        (
            Vector2f(0, 0),
            Region2f(
                Vector2f(0, 0),
                Vector2f(5, 5),
            ),
        ),
        (
            Vector2f(2, 3),
            Region2f(
                Vector2f(2, 3),
                Vector2f(3, 2),
            ),
        ),
        (
            Vector2f(3, 2),
            Region2f(
                Vector2f(3, 2),
                Vector2f(2, 3),
            ),
        ),
        (
            Vector2f(2, 2),
            Region2f(
                Vector2f(2, 2),
                Vector2f(3, 3),
            ),
        ),
        (
            Vector2f(3, 3),
            Region2f(
                Vector2f(3, 3),
                Vector2f(2, 2),
            ),
        ),
        (
            Vector2f(4, 4),
            Region2f(
                Vector2f(3, 3),
                Vector2f(2, 2),
            ),
        ),
        (
            Vector2f(5, 5),
            Region2f(
                Vector2f(3, 3),
                Vector2f(2, 2),
            ),
        ),
        (
            Vector2f(5, 6),
            Region2f(
                Vector2f(3, 3),
                Vector2f(2, 3),
            ),
        ),
        (
            Vector2f(5, 7),
            Region2f(
                Vector2f(3, 3),
                Vector2f(2, 4),
            ),
        ),
        (
            Vector2f(2, 7),
            Region2f(
                Vector2f(2, 3),
                Vector2f(3, 4),
            ),
        ),
        (
            Vector2f(6, 5),
            Region2f(
                Vector2f(3, 3),
                Vector2f(3, 2),
            ),
        ),
        (
            Vector2f(6, 6),
            Region2f(
                Vector2f(3, 3),
                Vector2f(3, 3),
            ),
        ),
    ],
)
def test_accommodate(point: Vector2f, expect: Region2f) -> None:
    region = Region2f(
        Vector2f(3, 3),
        Vector2f(2, 2),
    )

    result = region.accommodate(point)

    assert result == expect


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
