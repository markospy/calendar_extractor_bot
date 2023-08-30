from selenium.common.exceptions import WebDriverException
from calendario.interfaz import Interfaz, scraping

from calendario.calendario import Calendario

if __name__ == "__main__":
    try:
        program = Interfaz()
        program.menu()
        program.record_config()
        scraping(program.path)
        program.programar_rapado()

    except Exception as e:
        if "in PATH" in str(e):
            print(
                "You are try to run the bot from command line \n"
                "Please add to PATH your Selenium Drivers \n"
                "Windows: \n"
                "       set PATH=%PATH%;C:path-to-your-folder \n\n"
                "Linux: \n"
                "       PATH=$PATH:/path/toyour/folder/ \n"
            )
        else:
            raise
    else:
        print("Error de conexión. Revise su internet")
