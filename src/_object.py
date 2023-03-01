from _behavior import Behavior


class Object:
    behaviors: list[Behavior]

    def __init__(self) -> None:
        self.behaviors = []

    def register(self, behavior: Behavior) -> None:
        self.behaviors.append(behavior)
