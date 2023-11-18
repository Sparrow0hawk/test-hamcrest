class Cutlery:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        raise NotImplementedError
