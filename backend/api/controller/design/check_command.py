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
        
class CheckUsernameCommand(CheckCommand):
    def __init__(self, email : str):
        self.email = email
    def execute(self):
        invoker = Invoker()
        whatever = WordFilter("@", self.email)
        invoker.set_command(whatever)
        invoker.execute_command()
        
class WordFilter(CheckCommand):
    with open("FORBIDDENWORDSLIST.txt", "r") as file:
        temp = file.readlines()
    """this reads from the forbiddenwordslist file line by line"""
    FORBIDDEN_WORDS = [word.strip() for word in temp]
    """this makes it so the whitespaces and the newlines disappear and shi"""

   
    def __init__(self, delimiter : str, texts : str):
        self.delimiter = delimiter
        self.forbiddenWords = [word.lower() for word in WordFilter.FORBIDDEN_WORDS]
        self.text = texts

    def extract(self, text : str) -> str:
        """This thing just extracts whatever comes before the delimiter and stuff"""
        index = text.find(self.delimiter)
        """If it finds the delimiter in the passed string, it will return an index to where the delimiter is and then it will return everything before the index
            if it cant find the delimiter it just passes the entire string raw and unchanged
        """
        if index != -1:
            return text[:index]
        else:
            return text
        
    def hasForbiddenWord(self, text : str) -> bool:
        """checks if the seperated partition is free from slurs, if free then it will return true otherwise false"""
        partition = self.extract(text).lower()
        check = any(word in partition for word in self.forbiddenWords)
        return check
        
    def __iter__(self):
        return iter(self.forbiddenWords)
    
    def execute(self) -> bool:
        if self.hasForbiddenWord(self.text):
            print("you said bad word bro make it again")
            return False
        else:
            print("ok yeah this works")
            return True
