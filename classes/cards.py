import random


class Card:
    def __init__(self, naipe, numero, cor):
        self.naipe = naipe
        self.numero = numero
        self.cor = cor

    def __str__(self):
        return f"{self.numero} de {self.naipe}, cor {self.cor}"


class Baralho:
    def __init__(self):
        self.cartas = []

        naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        numeros = range(1, 14)
        cores = ["Vermelho", "Preto"]

        for nipe in naipes:
            for num in numeros:
                # Define a cor da carta baseado no naipe
                cor = "Vermelho" if nipe in ["Copas", "Ouros"] else "Preto"
                self.cartas.append(Card(nipe, num, cor))

    def distribuir_cartas(self, quantidade=5):
        if quantidade > len(self.cartas):
            raise ValueError("Não há cartas suficientes no baralho para distribuir.")

        cartas_distribuidas = random.sample(self.cartas, quantidade)
        for carta in cartas_distribuidas:
            self.cartas.remove(carta)

        return cartas_distribuidas
