from config.logger import Logger

class SistemaConfig:            # Singleton con la configuración global
    _inst = None
    def __new__(cls):
        if cls._inst is None: 
            cls._inst  = super().__new__(cls) 
            cls._inst.nombre  = "Sistema de Gestión Cursos y Estudiantes"  
            cls._inst.version = "1.0"
            cls._inst.empresa = "ISTP Argentina"
            cls._inst.autor ="Tello Luis - Castro Raquel"
            Logger().info(f"Sistema Inicado :{cls._inst.nombre} Version :{cls._inst.version} Empresa :{cls._inst.empresa} Autor :{cls._inst.autor}")
        return cls._inst     
class Alumno:

    # Constructor
    def __init__(self, codigo_alumno="", id_persona=0, id_distrito=0):

        self.__id_alumno = 0
        self.__codigo_alumno = codigo_alumno
        self.__id_persona = id_persona
        self.__id_distrito = id_distrito

    # Getter y Setter del ID
    @property
    def id_alumno(self):
        return self.__id_alumno
