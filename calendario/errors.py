class Error(Exception):
    def __init__(self, message="Ha ocurrido durante el manejo de los datos extraidos!"):
        super().__init__(message)
