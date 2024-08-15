import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result, description",
    [
        (14, 14, [0, 0], "Age less than 15 should return [0, 0]"),
        (23, 23, [1, 1], "Age equals to 23 return [1, 1]"),
        (24, 24, [2, 2], "When age 24 should return [2, 2]"),
        (-1, -1, [0, 0], "Negative ages should return [0, 0]"),
        (
            17,
            17,
            [1, 1],
            "When age equals to 15 and less than 24 should return [1, 1]",
        ),
        (
            100,
            100,
            [21, 17],
            "When age 100 should return 21 for cat and 17 for dog",
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list,
        description: str,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result, description


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("five", "five"),
        (None, None),
    ]
)
def test_human_age_for_invalid_input(
        cat_age: str | None,
        dog_age: str | None,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
