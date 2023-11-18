from src.test_hamcrest.cutlery import Cutlery


class Fork(Cutlery):
    def __init__(self, name: str):
        super().__init__(name=name)

    @property
    def name(self):
        return self._name
