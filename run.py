from selenium.common.exceptions import WebDriverException
from calendario.interfaz import Interfaz, scraping
from calendario.calendario import Calendario

from calendario.calendario import Calendario

if __name__ == "__main__":
    program = Interfaz()
    program.menu()
    program.record_config()
    scraping(program.path)
    program.programar_rapado()
