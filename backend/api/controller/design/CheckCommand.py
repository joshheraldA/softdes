from abc import ABC, abstractmethod

class CheckCommand(ABC):

    @abstractmethod

    def execute(self) -> bool:
        pass

class CheckEmail(CheckCommand):
    """Check the email to see if its a valid email"""
    def __init__(self, email):
        self.email = email
    
    def execute(self) -> bool:
        """
            Execute the individual command of each subcommands
            Args:
                None
            
            Returns:
                conditionMet (boolean): Chcek if conditions are met
        """
        if "@usc.edu.ph" in self.email:
            return True            

        print("Missing @ in parameters")
        return False
        

class Invoker:
    def __init__(self):
        self._command = None
    
    def set_command(self, command : CheckCommand) -> bool: 
        """
            Set the typ of command you want
            Arg:
                command (CheckCommand, required): the command you want the invoker to invoke
            Returns:
                bool: True if command field is given, othrewise False
            
        """
        if command is None:
            print("command field required")
            return False        

        self._command = command
        return True

    def execute_command(self) -> bool:
        """
        Execute the command Invoker is given
        Args:
            None
        Returns:
            bool: Returns a boolean to whether or not the condition is set
        """
        if self._command:
            return self._command.execute()

