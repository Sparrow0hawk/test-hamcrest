from hamcrest import assert_that, equal_to

from test_hamcrest import Fork


def test_forks_have_same_name_hamcrest():
    small_fork = Fork("small")

    assert_that(small_fork.name, equal_to("small"))


def test_forks_have_same_name_vanilla():
    small_fork = Fork("small")

    assert small_fork.name == "small"
