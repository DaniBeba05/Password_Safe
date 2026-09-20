
class Password: 

    def __init__(self, contraseña, num_intentos, intentos_maximos = 3, minimo = 12):
        self.contraseña = contraseña
        self.num_intentos = num_intentos
        self.intentos_maximos = intentos_maximos
        self.minimo = minimo


    def introducirpassword(self):
    
        self.contraseña = str (input("Password:"))
    
        return self.contraseña

    
    def tiene_longitud_maxima (self):

        return len (self.contraseña) >= self.minimo

    

    def tiene_una_mayuscula (self):
    
        return any(caracter.isupper() for caracter in self.contraseña)

    

    def tiene_un_numero (self):
   
        return any (caracter.isdigit() for caracter in self.contraseña)


    def tiene_un_simbolo (self):

        simbolos = '.,@#?!>;:-_'

        return any(caracter in simbolos for caracter in self.contraseña)

    

    def comprobar_num_intentos(self):

        return self.num_intentos < self.intentos_maximos


    def sumar_num_intentos (self):

        self.num_intentos+=1


    def comprobar_password_valida(self):

        return (self.tiene_longitud_maxima() and self.tiene_una_mayuscula() and self.tiene_un_numero() and self.tiene_un_simbolo())

    def mensajedepasswordvalida(self):
         
        return "La contraseña introducida es valida"

    
    def mensajedesuperaciondeintentos(self):

        return "Has superado el número de intentos posibles. Vuelve a intentarlo más tarde"



    def mensajerequisitomayuscula(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos una mayúscula"



    def mensajerequisitonumero(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos un número"



    def mensajerequisitosimbolo(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos un simbolo"



    def mensajerequisitonumcaracteres(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos 12 carácteres"



   
