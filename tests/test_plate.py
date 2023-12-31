import pytest
from hamcrest import assert_that, equal_to, has_properties

from test_hamcrest import Fork, Knife
from test_hamcrest.plate import Plate


def test_plate() -> None:
    fork = Fork("small")
    knife = Knife("large")
    plate = Plate(meal="Dinner", left=fork, right=knife)

    assert_that(plate, has_properties(meal=equal_to("Dinner"), left=equal_to(fork), right=equal_to(knife)))


@pytest.mark.xfail
def test_plate_fails_with_different_instance() -> None:
    fork = Fork("small")
    knife = Knife("large")
    plate = Plate(meal="Dinner", left=fork, right=knife)

    assert_that(
        plate, has_properties(meal=equal_to("Dinner"), left=equal_to(Fork("small")), right=equal_to(Knife("large")))
    )
