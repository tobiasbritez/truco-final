import random
from typing import List, Tuple

def crear_mazo() -> List[Tuple[int, str]]:
    """
    Crea un mazo con las cartas y sus respectivos valores para Truco y Envido.
    """
    palos = ['Espadas', 'Bastos', 'Oros', 'Copas']
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

    # Construcción del mazo (valor numérico real y su palo)
    mazo = [(valor, palo) for palo in palos for valor in valores]

    # Barajar el mazo
    random.shuffle(mazo)
    return mazo

def valor_envido(carta: Tuple[int, str]) -> int:
    """
    Retorna el valor de la carta para el Envido:
    - 10, 11, 12 valen 0 para el Envido.
    """
    valor, _ = carta
    return valor if valor <= 7 else 0


def fuerza_truco(carta: Tuple[int, str]) -> int:
    """
    Retorna la fuerza de la carta según las reglas del Truco.
    A menor número, mayor fuerza.
    """
    valor, palo = carta
    jerarquia = {
        (1, 'Espadas'): 1,  # As de Espadas (más fuerte)
        (1, 'Bastos'): 2,
        (7, 'Espadas'): 3,
        (7, 'Oros'): 4,
        (3, 'Espadas'): 5, (3, 'Bastos'): 5, (3, 'Oros'): 5, (3, 'Copas'): 5,
        (2, 'Espadas'): 6, (2, 'Bastos'): 6, (2, 'Oros'): 6, (2, 'Copas'): 6,
        (1, 'Oros'): 7, (1, 'Copas'): 7,
        (12, 'Espadas'): 8, (12, 'Bastos'): 8, (12, 'Oros'): 8, (12, 'Copas'): 8,
        (11, 'Espadas'): 9, (11, 'Bastos'): 9, (11, 'Oros'): 9, (11, 'Copas'): 9,
        (10, 'Espadas'): 10, (10, 'Bastos'): 10, (10, 'Oros'): 10, (10, 'Copas'): 10,
        (7, 'Copas' ): 11, (7, 'Bastos' ): 11,
        (6, 'Espadas'): 12, (6, 'Bastos'): 12, (6, 'Oros'): 12, (6, 'Copas'): 12,
        (5, 'Espadas'): 13, (5, 'Bastos'): 13, (5, 'Oros'): 13, (5, 'Copas'): 13,
        (4, 'Espadas'): 14, (4, 'Bastos'): 14, (4, 'Oros'): 14, (4, 'Copas'): 14,  # 4 (menos fuerte)
    }
    return jerarquia.get((valor, palo), 15)  # Si no está definido, menor prioridad