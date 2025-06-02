# Basic Foo StdClass like stuff
# SINCE 2025-02-03
# AUTHOR Sven Schrodt



class StdCls:
    """ Container Class 
        - in memoriam of PHP: 
            - stdClass
            - including its (PHP's) functionality:
                - like var_dump() 
                - like print_r()     
    """
    def dmp(self) -> dict:
        return (vars(self))

ob = StdCls()

ob.name ='Robbi'
ob.buddy ='Tobbi'
ob.vehicle ='Fliewatüüt' #°^
ob.born = '1967'
ob.id = 4231109

dmp = ob.dmp()
print(dmp)
print(type(dmp))






#°^ in de: #  _Flie_gen, _Wa_sser, _tüüt_ (PKW Hupe)