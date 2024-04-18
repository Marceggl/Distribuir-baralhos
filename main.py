from classes.cards import *


def main():
    baralho = Baralho()
    cartas_distribuidas = baralho.distribuir_cartas()
    print("Cartas distribuídas:")
    for carta in cartas_distribuidas:
        print(carta)


if __name__ == "__main__":
    main()
