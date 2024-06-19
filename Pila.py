from Nodo import Nodo
from Producto import Producto

class Pila:
    def __init__(self) -> None:
        self.cima = None
        
    def esta_vacia(self):
        return self.cima is None
    
    def push(self, valor : Producto):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cima = nuevo_nodo
        else: 
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo
            
    def pop(self):
        if self.esta_vacia():
            print('La pila está vacía')
            return
        else:
            valor = self.cima.valor
            self.cima = self.cima.siguiente
            return valor
        
    def top(self):
        if self.esta_vacia():
            print('La pila está vacía')
        else:
            return self.cima.valor.__str__()
        
    def inOrder(self):
        i = self.cima
        while i is not None:
            j = self.cima
            while j.siguiente is not None:
                valor1 = j.valor
                valor2 = j.siguiente.valor
                if valor1.precio > valor2.precio:
                    j.valor = valor2
                    j.siguiente.valor = valor1
                j = j.siguiente       
            i = i.siguiente
        
    def mostrar(self):
        string = ""
        actual = self.cima
        while actual:
            string += actual.valor.__str__() + '\n'
            actual = actual.siguiente
        return string
                
                
                
            