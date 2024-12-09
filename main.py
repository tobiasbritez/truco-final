from funciones.partida import jugar_partida
from funciones.ranking import actualizar_ranking, mostrar_ranking


def elegir_puntaje_juego() -> int:
    """
    Permite al jugador elegir si jugar a 15 o 30 puntos.
    """
    while True:
        try:
            puntos: int = int(input("¿A cuántos puntos quieres jugar? (15 o 30): ").strip())
            if puntos in [15, 30]:
                return puntos
        except ValueError:
            pass
        print("Número incorrecto. Por favor, elige 15 o 30.")


def main() -> None:
    """
    Función principal que ejecuta el flujo del juego.
    """
    print("¡Bienvenido al Truco Argentino!")
    nombre: str = input("Ingresa tu nombre: ").strip()

    # Elegir puntaje del juego
    puntaje_juego: int = elegir_puntaje_juego()

    # Inicializar los puntos
    puntos_humano: int = 0
    puntos_maquina: int = 0

    # Bucle principal del juego
    while puntos_humano < puntaje_juego and puntos_maquina < puntaje_juego:
        puntos_humano, puntos_maquina = jugar_partida(
            puntos_humano, puntos_maquina, puntaje_juego
        )
        print(f"\nPuntuación total: Tú {puntos_humano} | Máquina {puntos_maquina}")

    # Determinar el ganador final
    if puntos_humano >= puntaje_juego:
        print("\n¡Felicidades, ganaste el juego!")
        actualizar_ranking(nombre, puntos_humano)
    else:
        print("\nLa máquina gana el juego. ¡Intenta nuevamente!")

    # Mostrar el ranking al final del juego
    mostrar_ranking()

if __name__ == "__main__":
    main()
