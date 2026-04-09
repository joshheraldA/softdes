from random import randint, choices
import string

class IdFactory:
    def __init__(self, length=21, allow_letters=False):
        """
        Args:
            length (int, optional): Number of digit in the id. Defaults to 21
            allow_letters (boolean, optional): Sets it so that the id can accomodate letters. Defaults to False
        Funcions:
            create_id (int): Creates an id, no parameters required
        """
        self.length = length
        self.allow_letters = allow_letters


    def create_id(self):
        """
        Generates a random numeric ID.

        Args:
            None

        Returns:
            int | str: A random numeric ID (int) or alphanumeric ID (str)
                depending on allow_letters.        
        """

        if self.allow_letters:
            characters = string.ascii_letters + string.digits
            return ''.join(choices(characters, k=self.length))

        result = 0      # the id output
        exp = 1         # exponential increase each time 

        for i in range(self.length):    
            rand_num = randint(0, 9)        # creates a random number
            result += (rand_num * exp)      # multiples it by the exponential offset and adds its to the resulting id 
            exp *= 10                       # change the exponential offset (e.g 1, 10, 100)
        
        return result   # the id 

                