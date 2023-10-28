import pandas as pd
from typing import Optional, Any
from calendario.errors import Error


class DataframeCreator:
    """Toma una lista de listas emitidas por una instancia de
    Calendario que tiene la información referente al tiempo,
    la moneda y el impacto de la noticia y la convierte en un
    dataframe y lo guarda en un .csv antes o después de su
    procesamiento por una instancia de la clase ConvertNumber

    atributos:
        path: str. Dirección donde se guardará el .csv
        lista: list. Listas emitida por una instancia de Calendario.
        df_extern: Dataframe emitido por una instancia de ConvertNumber
        luego de su procesamieno.
    """

    def __init__(
        self, path: str, lista: list, df_extern: Optional[None | Any] = None
    ) -> None:
        self.df = self.create_df(lista)
        self.path = rf"{path}"
        self.df_extern = df_extern

    def create_df(self, lista):
        """Crea el dataframe a partir de la lista"""
        if len(lista[0]) > 0:
            lenth_list = len(lista[0])
            if all([len(x) == lenth_list for x in lista]):
                data = []
                for x in zip(*lista):
                    data.append(x)
                return pd.DataFrame(data)
            else:
                print(
                    f"Tamaño de la lista 1 ---> {len(lista[0])} \nTamaño de la lista 2 ---> {len(lista[1])} \nTamaño de la lista 3 ---> {len(lista[2])}"
                )
                raise Error()
        else:
            print("Tamaño de la lista ---> ", len(lista[0]))
            raise Error()

    def df_save_csv(self, dataframe):
        """Guarda el dataframe en un archivo .csv. Puede ser el dataframe
        creado por la misma clase o el recibido de la clase ConvertNumber
        """

        dataframe.to_csv(
            self.path + r"notices.csv",
            encoding="utf-8-sig",
            sep=",",
            index=False,
            header=False,
        )

        print("Scraping 🆗")
