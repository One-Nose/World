from datetime import timedelta

from _object import Object


class World:
    objects: list[Object]
    time: timedelta

    def __init__(self) -> None:
        self.objects = []
        self.time = timedelta()

    def register(self, obj: Object) -> None:
        self.objects.append(obj)
