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
        
        
myerror = ERROR_EVENT(maasage=" importand data is missing ", code='1.0.0', typeevent='Usererror')
print(type(myerror))
if isinstance(myerror, ERROR_EVENT):
    print(myerror.ERROR_MASSAGE)