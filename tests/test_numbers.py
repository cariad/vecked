from pytest import mark

from vecked import TNumeric, distance_between


@mark.parametrize(
    "a, b, expect",
    [
        (0, 0, 0),
        (0, 1, 1),
        (-1, 0, 1),
        (1, 1, 0),
        (1, 3, 2),
        (3, 1, 2),
        (-1, 5, 6),
        (-5, 1, 6),
        (-5, -8, 3),
        (-8, -5, 3),
        (0, 0.5, 0.5),
        (0.5, 0, 0.5),
        (1.25, 2.0, 0.75),
        (-1.25, -2.75, 1.5),
    ],
)
def test_distance_between(
    a: TNumeric,
    b: TNumeric,
    expect: TNumeric,
) -> None:
    assert distance_between(a, b) == expect
