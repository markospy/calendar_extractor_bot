from selenium.common.exceptions import WebDriverException
from calendario.interfaz import Interfaz, scraping

if __name__ == "__main__":
    try:
        program = Interfaz()
        program.menu()
        program.record_config()
        scraping(program.path)
        program.programar_rapado()
    except WebDriverException:
        print("Ha ocurrido un error! Revise su conexión.")
# Ejecutar esto en terminal
