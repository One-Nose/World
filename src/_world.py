from datetime import timedelta

from ._interfaces import ObjectInterface, WorldInterface


class World(WorldInterface):
    def __init__(self) -> None:
        self.objects = []
        self.time = timedelta()

    def register(self, obj: ObjectInterface) -> None:
        obj.world = self
        self.objects.append(obj)

    def step(self) -> None:
        pass
