## Bot Extractor de Noticias de Forex versión 0.2

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