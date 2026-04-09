from abc import ABC, abstractmethod
from typing import Any

import check_command


class Handler(ABC):
    @abstractmethod 
    def set_next_handler(self, handler: Handler) -> None:
        pass

    @abstractmethod
    def handle(self, request: Any) -> None:
        pass

class AbstractHandler(Handler):
    """
    The abstract handler as the main class that all subclass will refer to 
    Attributes:
        _next_handler 
    """
    _next_handler: Handler = None


    def set_next_handler(self, handler) -> Handler:
        self._next_handler = handler

        return handler

    def handle(self):
        if self._next_handler:
            return self._next_handler.handle()
        

class CheckCommandHandler(AbstractHandler):
    """
    This feature createst a chain of rseponsibility for multiple different Command Checker classes.
    Like what the name statese, it performs sequential functions while only having to call minimal code
    Attributes:
        request (Invoker, required): The function you want to Check Common Handle
    Methods:
        handle(None) -> bool: 
            handles the check command request and performs the given function     
    """
    def __init__(self, request: check_command.Invoker):
        self.request = request
     
    def handle(self) -> bool:
        """
        this handles the check command request and performs the given function
        Args: 
            None
        Returns::
            bool: True if the checker that the Invoker invokes is met, False otherwise
        """
        super().handle()
        return (self.request).execute_command()        


if __name__ == '__main__':
    email1 = "joshherald19@gmail.com"
    email2 = "24100598@usc.edu.ph"

    invoker1 = check_command.Invoker()
    invoker2 = check_command.Invoker()

    invoker1.set_command(check_command.CheckEmail(email1))
    check_command_handler1 = CheckCommandHandler(invoker1)

    invoker2.set_command(check_command.CheckEmail(email2))
    check_command_handler2 = CheckCommandHandler(invoker2)


    check_command_handler1.set_next_handler(check_command_handler2)

    check_command_handler1.handle()