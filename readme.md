## Bot Extractor de Noticias de Forex versión 0.2

### Index:
[Español](#español-id)  
[English](#english-id)


<h3 id="español-id">Español</h3>

Este bot🤖 esta programado con selenium. Basicamente lo que hace es entrar al calendario de noticias de la página de [MQL5](https://www.mql5.com/es/economic-calendar "https://www.mql5.com/es/economic-calendar")  y extraer la noticias de mediano y alto impacto de las monedas de mayor liquidez: Euro, Libra, Dolar, Dolar Canadiense, Dolar neozelandes y Franco suizo.

Fue programado con el objetivo de generar un .csv a consumir por un bot de metatrader 4 y 5 que se encarga de apagar el trading automático cuando se acerca un fundamental.

Antes de ejecutarlo deberás aseguarte de cumplir con las siguientes especificaciones:

* python>=3.10 o mayor
* selenium==4.4.3
* pandas==1.5.3
* schedule==1.2.0

Para correrlo debes ejecutar el archivo `run.py` en la línea de comando:

    python run.py

Deberás configurar el bot en el menú interactivo de la línea de comandos. Podrás escoger la frecuencia de raspado y la carpeta a donde se guardará el alrchivo notices.csv que contendrá las noticias. El mismo se reescribirá con cada nuevo raspado.

Asegurate de que el directorio que proporciones termine con "\\". Ejemplo:

    C:\Users\Marcos\Desktop\

El .csv tendrá 4 columnas: hora, impacto, moneda y día de la semana. El día de la semana tomará un valor entre 0 y 6, de lunes a sábado.

*Espero que te sea de utilidad. Cualquier recomendación o mejora será bien recibida.*


<h3 id="english-id">English</h3>

This bot 🤖 is programmed with selenium. Basically what it does is to enter the news calendar of the [MQL5](https://www.mql5.com/es/economic-calendar "https://www.mql5.com/es/economic-calendar") and extract the medium and high impact news from the most liquid currencies: Euro, Pound, Dollar, Canadian Dollar, New Zealand Dollar and Swiss Franc.

It was programmed with the aim of generating a.csv to be consumed by a metatrader 4 and 5 bot that is responsible for turning off automatic trading when a fundamental is approaching.

Before executing it you must make sure that you meet the following specifications:

* python>=3.10 or higher
* selenium==4.4.3
* pandas==1.5.3
* schedule==1.2.0

To run it you must run the file `run.py ` on the command line:

    python run.py

You will need to configure the bot in the interactive menu of the command line. You will be able to choose the frequency of scraping and the folder to which the notices file will be saved.csv that will contain the news. The same will be rewritten with each new scraping.

Make sure that the directory you provide ends with "\\". Example:

    C:\Users\Marcos\Desktop\

The.csv will have 4 columns: time, impact, currency and day of the week. The day of the week will take a value between 0 and 6, from Monday to Saturday.

*I hope it will be useful to you. Any recommendations or improvements will be welcomed.*