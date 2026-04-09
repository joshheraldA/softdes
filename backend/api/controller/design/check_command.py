from abc import ABC, abstractmethod

class CheckCommand(ABC):

    @abstractmethod
    def execute(self) -> bool:
        pass

class CheckEmailCommand(CheckCommand):
    """
    Check the email to see if its a valid email
    Attributes:
        email (str, required): the email you want to verify
    Methods: 
        execute(email: str) -> bool:
            executes its command to check if conditions satisfy. If satisfiees, it returns True, False otherwise
    """
    def __init__(self, email : str) -> None:

        self.email = email
    
    def execute(self) -> bool:
        """
            Execute the individual command of each subcommands
            Args:
                None
            Returns:
             bool: Chcek if conditions are met
        """
        if "@usc.edu.ph" in self.email:
            print(f"{self.email} is a valid email")
            return True            

        print(f"{self.email} is Missing @usc.edu.ph in parameters")
        return False

class Invoker:
    """
        A class that invokes commands dynamically depending on user's choices

    Attributes: 
        _command (CheckCommand): The internal storage for the assigned command.   

    Methods:
        set_command(command: CheckCommand) -> bool: 
            sets the CheckCommand that invoker is gonna invoke
        execute_command(None) -> bool: 
            execute the CheckCommand that the invoker is assigned to. Returns False there is no command assigned to it  
    """
    def __init__(self):

        self._command = None
    
    def set_command(self, command : CheckCommand) -> bool: 
        """
            Set the typ of command you want

            Args:
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
        

    
if __name__ == '__main__':
    invoker = Invoker()

    emailChecker = CheckEmailCommand("samisgay@email.com")
    invoker.set_command(emailChecker)
    invoker.execute_command()



    emailChecker2 = CheckEmailCommand("24100598@usc.edu.ph")
    invoker.set_command(emailChecker2)
    invoker.execute_command()