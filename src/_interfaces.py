from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import timedelta


class BehaviorInterface(ABC):
    pass


class ObjectInterface(ABC):
    world: WorldInterface
    behaviors: list[BehaviorInterface]

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def register(self, behavior: BehaviorInterface) -> None:
        pass


class WorldInterface(ABC):
    objects: list[ObjectInterface]
    time: timedelta

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def register(self, obj: ObjectInterface) -> None:
        pass

    @abstractmethod
    def step(self) -> None:
        pass
