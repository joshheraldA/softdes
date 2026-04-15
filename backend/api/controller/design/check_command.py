from abc import ABC, abstractmethod

from typing import Optional

from api.firebase import db
from firebase_admin import auth
class CheckCommand(ABC):

    @abstractmethod
    def execute(self) -> bool:
        pass

# class CheckPasswordUsername(CheckCommand):
#     """
#     checks if username and password is correct

#     Attributes
#     ----------
#     username: str
#         the username of an account
#     password: str
#         th password of an account

#     Methods
#     -------
#     execute():
#         Checkcs if the username and password of the account matches
#     """

#     def __init__(self, username: str, password: str):

#         self.username = username
#         self.password = password


#     def execute(self) -> bool:
#         users_ref = db.collection('users')

#         query = users_ref.where(filter=FieldFilter('username', '==', self.username)).limit(1).get()
#         if not query:
#             return False

#         users_doc = query[0].to_dict()
#         print(f"DEBUG: Full document data: {users_doc}") # Add this line
#         stored_password = users_doc.get('password')

#         print(stored_password)

#         return stored_password == self.password

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
            Set the type of command you want

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
    def __init__(self, username : str):
        self.username = username

    def execute(self):
        filter_command = WordFilter("@", self.username)
        return filter_command.execute()
    
class WordFilter(CheckCommand):
    """
    This filters words based on what is passed

    Attributes:
        text (str): This a text that you want to limit
        FORBIDDEN WORDS ([str]): List of forbidden words that the text cannot have
    """
   
    def __init__(self, texts : str):
        self.forbiddenWords = self.extract_word_file()
        self.text = texts

    def extract_word_file() -> list:
        with open("FORBIDDENWORDSLIST.txt", "r") as file:
            temp = file.readlines()
        
        FORBIDDEN_WORDS = [word.strip() for word in temp]
        return FORBIDDEN_WORDS

    def delimiter(self, delimiter: str) -> Optional[str]:
        """
            This method delimits the email to its userename

            Args:
                delimiter (str): the index to where you limit th text

            Returns:
            str
        """
        index = (self.text).find(self.delimiter)

        if index != -1:
            return self.text[:index]
        else:
            return None
        
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

