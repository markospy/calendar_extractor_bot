import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from calendario.constants import BASE_URL
from selenium.common.exceptions import NoSuchElementException


class Calendario(webdriver.Chrome):
    """Extraer datos de las noticias de mediano y alto impacto"""

    def __init__(self, driver_path="C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardow = teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        super(Calendario, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()
        self.hours = []
        self.importances = []
        self.flags = []

    def __exit__(self, exc_type, exc, traceback):
        if self.teardow:
            self.quit()

    def land_first_page(self):
        """Carga la página web"""
        print("Scraping...⏰")
        self.get(BASE_URL)

    def check_cookies(self):
        """Checa la aparición de los cookies"""
        try:
            if self.find_element(
                By.CSS_SELECTOR, "div.float-vertical-panel"
            ).is_displayed():
                cookies_close = self.find_element(
                    By.CSS_SELECTOR, "span.float-vertical-panel__cross"
                )
                cookies_close.click()
        except NoSuchElementException:
            pass

    def select_date_range(self):
        """Selecciona el rango de fecha semanal"""
        selection_date_range = self.find_element(
            By.CSS_SELECTOR, 'label[for="filterDate1"]'
        )
        if selection_date_range.get_attribute("class") != "checked":
            selection_date_range.click()

    def select_importance_event(self):
        """"""
        state_importance_event = self.find_elements(
            By.CSS_SELECTOR, 'input[name="importance"]'
        )

        checkbox__importance_event = []
        for i in range(1, 9):
            if i in [1, 2, 4, 8]:
                checkbox__importance_event.append(
                    self.find_element(
                        By.CSS_SELECTOR, f'label[for="filterImportance{i}"]'
                    )
                )

        state_checkbox = [
            (state, checkbox)
            for state, checkbox in zip(
                state_importance_event, checkbox__importance_event
            )
        ]

        count = 0
        for option in state_checkbox:
            count += 1
            if count == 3:
                break

            if (
                option[0].get_attribute("checked")
                and option[1].get_attribute("for") == f"filterImportance{count}"
            ):
                option[1].click()

    def select_flags(self):
        """Filta las monedad de mayor líquidez: EUR, GBP, USD, AUD,
        CAD, CHF, NZD, JPY"""
        selection_flags = self.find_elements(
            By.CSS_SELECTOR, "#economicCalendarFilterCurrency label"
        )

        for i in selection_flags:
            if i.text.strip()[0:3] not in [
                "EUR",
                "GBP",
                "USD",
                "AUD",
                "CAD",
                "CHF",
                "NZD",
                "JPY",
            ]:
                sleep(1)
                i.click()

    def extract_hours(self):
        """Extrae la horas de cada noticia"""
        sleep(15)
        _hours = self.find_elements(By.CSS_SELECTOR, ".ec-table__col_time")
        for hour in _hours:
            if hour.text == "Todo el día":
                self.hours.append(hour.text)
                print(type(hour.text))
            elif hour.text.endswith("(prov.)"):
                self.hours.append(hour.text[0:5])
            elif hour.text != "" and len(hour.text) <= 5:
                self.hours.append(hour.text)

    def extract_flags(self):
        """Extrae la moneda que afecta cada noticia"""
        _flags = self.find_elements(By.CSS_SELECTOR, ".ec-table__curency-name")
        for flag in _flags:
            self.flags.append(flag.text)

    def extract_importances(self):
        """Extrae la importancia de cada noticia"""
        _importances = self.find_elements(
            By.CSS_SELECTOR,
            ".ec-table__col.ec-table__col_time span",
        )
        for importance in _importances:
            if importance.get_attribute("title") != "":
                self.importances.append(importance.get_attribute("title"))
