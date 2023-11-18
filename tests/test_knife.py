from hamcrest import assert_that, equal_to

from test_hamcrest import Knife


def test_knife_have_same_name_hamcrest():
    knife = Knife("small")

    assert_that(knife.name, equal_to("small"))


def test_knife_have_same_name_vanilla():
    knife = Knife("small")

    assert knife.name == "small"
