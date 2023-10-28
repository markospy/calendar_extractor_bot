import pandas as pd


class Format:
    """Prepara el dataframe creado por DataframeCreator.

    La lista deberá contener la información en este orden:
    [hours, importances, flags]
    """

    def __init__(self, dataframe) -> None:
        self.df = dataframe

    def clear_df(self):
        """Limpia el dataframe de los eventos que se toman todo el día."""
        eliminar = self.df.loc[self.df[0] == "Todo el día"]
        self.df = self.df.drop(eliminar.index)
        self.df.reset_index(inplace=True, drop=True)
        self.df[0] = pd.to_datetime(self.df[0])

    def df_time_to_number(self):
        """Desecha la fecha y se queda solo con la hora en formato HH:MM"""
        for i in range(self.df.shape[0]):
            hour = str(pd.to_datetime(self.df.iloc[i, 0]).hour)
            minute = str(pd.to_datetime(self.df.iloc[i, 0]).minute)

            if len(minute) < 2:
                minute = "0" + minute
            if len(hour) < 2:
                hour = "0" + hour
            print(hour, ":", minute)

            self.df.iloc[i, 0] = hour + ":" + minute

    def df_day_to_number(self):
        """Crea una columna con el día de la semana en forma de número entero.
        Empieza con domingo 0 y termina con sábado 6.
        """
        self.df[3] = 0
        day = 0
        for i in range(self.df.shape[0]):
            if i > 0:
                hora_actual = self.df.iloc[i - 1, 0]
                hora_posterior = self.df.iloc[i, 0]
                if hora_posterior.hour >= hora_actual.hour:
                    self.df.iloc[i, 3] = day
                else:
                    day += 1
                    self.df.iloc[i, 3] = day
            elif i == 0:
                self.df.iloc[i, 3] = day
        self.df.drop(self.df[self.df[3] >= 5].index, inplace=True)
