class Producto:
    def __init__(self, nombre : str, precio : int) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"Producto: {self.nombre}. Precio: {self.precio}"