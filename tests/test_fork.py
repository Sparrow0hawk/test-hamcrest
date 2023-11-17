from hamcrest import assert_that, equal_to
from test_hamcrest import Fork


def test_forks_have_same_name():
    small_fork = Fork("small")
    big_fork = Fork("small")
    assert_that(small_fork.name, equal_to("small"))
