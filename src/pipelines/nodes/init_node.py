from src.pipelines.base import BaseNode


class InitNode(BaseNode):
    def __init__(self, name: str):
        super().__init__(name)

    def run(self, *args, **kwargs):
        pass
