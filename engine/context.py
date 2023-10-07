from .strategy import Strategy


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_strategy(self) -> Strategy:
        return self._strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def run(self) -> None:
        self._strategy.run()
