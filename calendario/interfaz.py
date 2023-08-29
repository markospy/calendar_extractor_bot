import schedule
import time
from calendario.calendario import Calendario
from calendario.preparation import ConvertNumber
from calendario.dataframe_creator import DataframeCreator


def scraping(file_dir):
    with Calendario(teardown=True) as bot:
        bot.land_first_page()
        bot.check_cookies()
        bot.select_date_range()
        bot.check_cookies()
        bot.select_importance_event()
        bot.check_cookies()
        bot.select_flags()
        bot.check_cookies()
        bot.extract_hours()
        bot.check_cookies()
        bot.extract_importances()
        bot.check_cookies()
        bot.extract_flags()
        bot.check_cookies()
        print(len(bot.hours))
        print(len(bot.flags))
        print(len(bot.importances))
        creator = DataframeCreator(file_dir, [bot.hours, bot.importances, bot.flags])
        convert = ConvertNumber(creator.df)
        convert.clear_df()
        convert.df_time_to_number()
        convert.df_day_to_number()
        creator.df_save_csv(convert.df)


class Interfaz:
    def __init__(self) -> None:
        self.path = ""
        self.idioma = ""
        self.frecuencia = ""
        self.frecuencia_text = ""

    def menu(self):
        while self.idioma != "es" and self.idioma != "en" and self.idioma != "po":
            print("Seleccione su idioma")
            print("Select you lenguage")
            print("Selecione seu idioma")
            self.idioma = input("es | en | po\n>>> ").strip().lower()

            if self.idioma == "es":
                print("Frecuencia del scraping")
                while self.frecuencia != "1" and self.frecuencia != "2":
                    self.frecuencia = input("diaria(1) | semanal(2)\n>>> ").strip()
                self.path = input("Guardar archivo en: ")

            elif self.idioma == "en":
                print("Frecuency of scraping")
                while self.frecuencia != "1" and self.frecuencia != "2":
                    self.frecuencia = input("daily(1) | weekly(2)\n>>> ").strip()
                self.path = input("Save file in: ")

            elif self.idioma == "po":
                print("Frequência de rapagem")
                while self.frecuencia != "1" and self.frecuencia != "2":
                    self.frecuencia = input("diário(1) | semanal(2)\n>>> ").strip()
                self.path = input("Salvar arquivo em: ")

        match self.idioma:
            case "es":
                self.frecuencia_text = "diaria" if self.frecuencia == "1" else "semanal"
                print(
                    f"El scraping ha quedado programado\npara una frecuencia {self.frecuencia_text}."
                )
            case "en":
                self.frecuencia_text = "daily" if self.frecuencia == "1" else "weekly"
                print(
                    f"The scraping has been programmed\nfor a frequency {self.frecuencia_text}."
                )
            case "po":
                self.frecuencia_text = "diário" if self.frecuencia == "1" else "semanal"
                print(
                    f"A raspagem foi programada\npara uma frecuência {self.frecuencia_text}."
                )

    def programar_rapado(self):
        if self.frecuencia == "1":
            schedule.every().day.at("00:00").do(scraping)
        elif self.frecuencia == "2":
            schedule.every().monday.at("00:00").do(scraping)

        while True:
            schedule.run_pending()
            time.sleep(1)
