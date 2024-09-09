class RaizCuadrada:
    def __init__(self, valor):
        self.valor = valor
        self.aproximacion = 1.0

    def calcular_raiz(self, iteraciones):
        for k in range(1, iteraciones + 1):
            self.aproximacion = (self.aproximacion + self.valor / self.aproximacion) / 2
            print(f"La raíz cuadrada después de {k} iteraciones es: {self.aproximacion:.5f}")