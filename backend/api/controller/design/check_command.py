from abc import ABC, abstractmethod

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
    A class that checks email

    This class manages the email addresses to see if certain 
    conditions is satisfied 

    Attributes:
        email (str): The email address of the account
    """
    def __init__(self, email : str) -> None:

        self.email = email
    
    def execute(self) -> bool:
        """
        checks if the email addrss is a USC account

        This class implements a command pattern. It checks if the email address being pass contains **@usc.edu.ph**

        Args:
            None
        
        Returns
            bool: if th @usc.edu.ph is found inside the email address, False otherwise
        
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

