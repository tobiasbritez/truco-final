import random

def jugador_humano(cartas: list[tuple[int, str]]) -> tuple[int, str]:
    
    # función para que el jugador elija una carta.
    
    print('Tus cartas:', cartas)
    while True:
        try:
            eleccion: int = int(input('Elige una carta (1, 2 o 3): ')) - 1
            if 0 <= eleccion < len(cartas):
                return cartas.pop(eleccion)
        except ValueError:
            pass
        print('Selección inválida. Intenta nuevamente.')


def jugador_aleatorio(cartas: list[tuple[int, str]]) -> tuple[int, str]:
    
    # función para que un jugador aleatorio elija una carta de manera al azar.
    
    return cartas.pop(random.randint(0, len(cartas) - 1))
