class Persona:
    """Class con atributos básicos de una persona"""
    def __init__(self, nombre, genero, edad):
        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad
     #getters
        
    def get_nombre(self):
        return self.__nombre
    
    def get_genero(self):
        return self.__genero
    
    def get_edad(self):
        return self.__edad
    
    #Setters
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def set_genero(self, nuevo_genero):
        self.__genero = nuevo_genero
    
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad > 0:
           self.__edad = nueva_edad
        
        else: 
            print(f"Error: la edad debe ser un número entero positivo")
##############################################################################################   

class Estudiante(Persona):
    """Clase con atributos de estudiante"""
    def __init__(self, genero,nombre, edad):
        """Atríbutos únicos de estudiante"""
        super().__init__(nombre, genero, edad)
        self.__estudio = None 
        self.__estudiando = False
        
#getters
    def get__estudio(self):
        return self.__estudio
    
    def get__estudiando(self):
        return self.__estudiando
    
#setters

    def set_estudio(self, estudio):
        if isinstance(estudio, str) and estudio.lower() in ['primaria', 'bachiller', 'universitario']:
            self.__estudio = estudio
        else:
            print (f"Error: El estudio cursando debe de ser uno de estos tres valores: 'primaria', 'bachiller', 'universitario'")        
    
    def set_estudiando(self, estudiando):
        if isinstance(estudiando, bool):
            self.__estudiando = estudiando
        else:
            print(f"Error: este valor solo varia entre verdadero o falso")
  ##############################################################################################          
    
    def universitario(self): 
        """tipo de estudio universitario"""
        self.set_estudio("universitario")
        print(f"{self.get_nombre()} estudia como {self.get__estudio()} a la edad de {self.get_edad()}")
        
    def bachiller(self): 
        """tipo de estudio bachiller"""

        self.set_estudio("bachiller")
        print(f"{self.get_nombre()} estudia como {self.get__estudio()} a la edad de {self.get_edad()}")
        
    def primaria(self): 
        """tipo de estudio primaria"""
        self.set_estudio("primaria")
        print(f"{self.get_nombre()} estudia la {self.get__estudio()} a la edad de {self.get_edad()}")
        
    def estudiar(self):
        self.set_estudiando = True
        print(f"el estudiante {self.get_nombre()} se encuentra estudiando")
        
    def dejarestudiar(self):
        self.set_estudiando = False
        print(f"el estudiante {self.get_nombre()} ha dejado de estudiar")
        
estudiante1 = Estudiante("masculino", "pepe perez", "16")
estudiante1.bachiller()
estudiante1.estudiar()
estudiante1.dejarestudiar()

