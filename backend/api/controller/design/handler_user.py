from abc import ABC, abstractmethod
from typing import Any

from . import check_command


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
        return True

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
    def __init__(self, request: check_command.CheckCommand):
        self.invoker = check_command.Invoker()
        self.invoker.set_command(request)
     
    def handle(self) -> bool:   
        """
        this handles the check command request and performs the given function
        Args: 
            None
        Returns::
            result (bool): True if the checker that the Invoker invokes is met, False otherwise
        """
        result = (self.invoker).execute_command()     

        if not result:
            return False
        

        previous_result = super().handle()
        if not previous_result:
            return False 
        
        return result
