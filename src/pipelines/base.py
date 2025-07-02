from abc import ABC, abstractmethod
from enum import Enum


class NodeState(Enum):
    INIT = "init"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class BaseNode(ABC):
    def __init__(self, name: str):
        self.name = name
        self.state = NodeState.INIT

    @abstractmethod
    def run(self, *args, **kwargs):
        pass


class BasePipeline(ABC):
    def __init__(self, nodes: list[BaseNode]):
        self.nodes = nodes

    def run(self, *args, **kwargs):
        for node in self.nodes:
            node.run(*args, **kwargs)
