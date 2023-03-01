from _interfaces import BehaviorInterface, ObjectInterface


class Object(ObjectInterface):
    def __init__(self) -> None:
        self.behaviors = []

    def register(self, behavior: BehaviorInterface) -> None:
        self.behaviors.append(behavior)
