from datetime import datetime
from colorama import init, Fore
from abc import ABC, abstractmethod

init(autoreset=True)


class Logger(ABC):
    @abstractmethod
    def info(self, mensaje, objeto):
        pass

    @abstractmethod
    def warning(self, mensaje, objeto):
        pass

    @abstractmethod
    def error(self, mensaje, objeto):
        pass

    @abstractmethod
    def debug(self, mensaje, objeto):
        pass


class LoggerFactory(ABC):
    @abstractmethod
    def getLogger(self, tipo):
        pass


class LoggerFactoryImpl(LoggerFactory):

    def getLogger(self, tipo):
        # f file
        # c consola
        diccionario = {
            "c": LoggerConsola(),
            "f": LoggerFile(),
            "e": LoggerEmail()
        }
        return diccionario[tipo]


class LoggerConsola(Logger):
    def info(self, mensaje, objeto):
        print(datetime.now(), Fore.BLUE + "[INFO]", mensaje, objeto)

    def warning(self, mensaje, objeto):
        print(datetime.now(), Fore.YELLOW + "[WARN]", mensaje, objeto)

    def error(self, mensaje, objeto):
        print(datetime.now(), Fore.RED + "[ERROR]", mensaje, objeto)

    def debug(self, mensaje, objeto):
        print(datetime.now(), Fore.MAGENTA + "[DEB]", mensaje, objeto)


class LoggerFile(Logger):
    def info(self, mensaje, objeto):
        with open("file_log.txt", "a") as file:
            dato = (str(datetime.now()), 'INFO', mensaje + " " + str(objeto), "\n")
            file.writelines(dato)

    def warning(self, mensaje, objeto):
        with open("file_log.txt", "a") as file:
            dato = (str(datetime.now()), 'WARN', mensaje + " " + str(objeto), "\n")
            file.writelines(dato)

    def error(self, mensaje, objeto):
        with open("file_log.txt", "a") as file:
            dato = (str(datetime.now()), 'ERROR', mensaje + " " + str(objeto), "\n")
            file.writelines(dato)

    def debug(self, mensaje, objeto):
        with open("file_log.txt", "a") as file:
            dato = (str(datetime.now()), 'DEB', mensaje + " " + str(objeto), "\n")
            file.writelines(str(dato))


class LoggerEmail(Logger):

    def info(self, mensaje, objeto):
        print("Enviando email")

    def warning(self, mensaje, objeto):
        print("se encontro un warning")

    def error(self, mensaje, objeto):
        print("Se encontro un error enviando el email")

    def debug(self, mensaje, objeto):
        print("debug")


if __name__ == "__main__":
    type_log = input("Ingrese la letra 'c' para salida por consola, 'f' para el archivo o 'e' para email: ")
    logger = LoggerFactoryImpl().getLogger(tipo=type_log)
    logger.info("valor de variable", 223)
    logger.warning("valor de variable", 223)
    logger.error("valor de variable", 223)
    logger.debug("valor de variable", 223)
