# ============================================================
# Parcial 2 - Estructura de Datos I
# Código base final
# ============================================================


# ============================================================
# Punto 1: Lista Circular - Josephus modificado
# ============================================================

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m):
        if not self.head or self.head.next == self.head:
            return self.head
        current = self.head
        while current.next != self.head:
            current = current.next
            
        while current.next != current:
            for i in range(m - 1):
                current = current.next
            victima = current.next
            salto = victima.dato % 5 == 0 
            current.next = victima.next
            if salto:
                current = current.next
            self.head = current 
            return self.head         



# ============================================================
# Punto 2: Lista Simple - Método único
# ============================================================

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self):
        if not self.head or not self.head.next:
            return
        lento = self.head
        rapido = self.head
        while rapido.next and rapido.next.next:
            lento = lento.next
            rapido = rapido.next.next
        segunda_mitad = lento.next
        lento.next = None
        prev = None
        curr = segunda_mitad
        while curr:
            sig = curr.next
            curr.next = prev
            prev = None
            curr = segunda_mitad
        p1 = self.head
        p2 = prev
        while p2:
            sig1 = p1.next
            sig2 = p2.next
            p1.next = p2
            if sig1:
                p2.next = sig1
            p1 = sig1
            p2 = sig2





# ============================================================
# Pruebas base
# ============================================================

if __name__ == "__main__":

    print("===== Punto 1 =====")
    lista_c = ListaCircular()
    lista_c.crear_lista(7)
    lista_c.mostrar()

    sobreviviente = lista_c.josephus_modificado(3)
    print("Sobreviviente:", sobreviviente)


    print("\n===== Punto 2 =====")
    lista_s = ListaSimple()

    for x in [1, 2, 3, 4, 5, 6]:
        lista_s.insertar_final(x)

    lista_s.mostrar()

    lista_s.partir_voltear_intercalar()

    print("Resultado:")
    lista_s.mostrar()