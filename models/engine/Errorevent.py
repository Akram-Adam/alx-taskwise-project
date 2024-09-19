""" This module for the ERROR_EVENT class """




class ERROR_EVENT:
    """
    Class to handel Error massage
    This class Should handel the Error that will delever to the user 
    and the System failures
    - Frist Type : System failers
    - UserError : Error the should delver to the User
    """
    
    def __init__(self, maasage, code, typeevent, *args, **kwargs):
        """ 
        This is the constructor of the class
        - user : ERROR massage 
        - code of the Error
        - type of the Error
        """
        self.ERROR_MASSAGE = maasage
        self.ERROR_CODE = code
        self.ERROR_TYPE = typeevent
        
    def __str__(self) -> str:
        return f"[ERROR] '{self.ERROR_CODE}' :\n {self.ERROR_CODE}\n Type: {self.ERROR_MASSAGE}"
    
