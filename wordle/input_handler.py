import abc


class InputHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_input(self, *args, **kwargs) -> str:
        raise NotImplementedError()


class CliInputHandler(InputHandler):
    def get_input(self, *args, **kwargs) -> str:
        if len(args) <= 0:
            raise TypeError(f"{self.get_input.__name__} requires a message")
        message = args[0]
        return input(f'{message}: ').strip()
