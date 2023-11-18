from test_hamcrest.cutlery import Cutlery


class Plate:
    def __init__(self, meal: str, left: Cutlery, right: Cutlery):
        self._meal = meal
        self._left = left
        self._right = right

    @property
    def left(self) -> Cutlery:
        return self._left

    @property
    def right(self) -> Cutlery:
        return self._right

    @property
    def meal(self) -> str:
        return self._meal
