class KeySym:
    """ Class storing unicode representation of ´special´ keys on keyboards
    
        - esp. for fruity OSs like MacOS
    """
    APPLE_CMD = '⌘' # Command Key (⌘): U+2318
    APPLE_OPT = '⌥' # Option Key (⌥): U+2325
    APPLE_SFT = '⇧' # Shift Key (⇧): U+2312 
    
    def __init__(self):
        pass
    
    
print(KeySym.APPLE_CMD)
    
    