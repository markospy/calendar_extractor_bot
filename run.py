from calendario.interfaz import Interfaz, scraping

if __name__ == "__main__":
    program = Interfaz()
    program.menu()
    scraping(program.path)
    program.programar_rapado()
