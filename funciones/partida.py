from funciones.mazo import crear_mazo, fuerza_truco  # Importar la función de creación del mazo
from funciones.jugador import jugador_humano, jugador_aleatorio  # Funciones para las decisiones de los jugadores
from funciones.envido import gestionar_envido  # Función para manejar el envido
from funciones.truco import gestionar_truco, asignar_puntos_truco  # Función para manejar el truco
from typing import List, Tuple


def repartir_cartas(carta: List[Tuple[int, str]]) -> Tuple[List[Tuple[int, str]], List[Tuple[int, str]]]:
    """
    Reparte 3 cartas a cada jugador y retorna las manos.
    """
    return carta[:3], carta[3:6]  # Repartir las primeras 3 cartas a cada jugador


def jugar_partida(puntos_humano: int = 0, puntos_maquina: int = 0, puntaje_objetivo: int = 15) -> Tuple[int, int]:
    """
    Ejecuta una partida de truco entre el jugador y la máquina.
    Maneja el envido, los cantos del truco y las rondas de juego.
    """
    mano_actual = 'humano'  # Determina quién es mano en cada ronda

    while puntos_humano < puntaje_objetivo and puntos_maquina < puntaje_objetivo:
        # Crear y repartir el mazo
        mazo = crear_mazo()
        cartas_humano, cartas_maquina = repartir_cartas(mazo)

        print(f"\n{'Eres mano' if mano_actual == 'humano' else 'La máquina es mano'}")
        print(f"Tus cartas son: {cartas_humano}")
        print(f"Cartas de la máquina (ocultas durante el juego): {cartas_maquina}")

        # **1. Envido**
        puntos_envido_humano, puntos_envido_maquina = gestionar_envido(
            cartas_humano, cartas_maquina, puntos_humano, puntos_maquina, mano_actual
        )
        puntos_humano += puntos_envido_humano
        puntos_maquina += puntos_envido_maquina

        print(f"\nPuntuación tras el envido: Tú {puntos_humano} | Máquina {puntos_maquina}")

        # **2. Truco**
        truco_cantado = None
        rechazo = False

        truco_cantado, puntos_humano, puntos_maquina, rechazo = gestionar_truco(
            turno=mano_actual,
            truco_cantado=truco_cantado,
            puntos_humano=puntos_humano,
            puntos_maquina=puntos_maquina
        )

        # Si se rechaza el canto del Truco, pasar a la siguiente mano
        if rechazo:
            mano_actual = "humano" if mano_actual == "maquina" else "maquina"
            continue

        # **3. Rondas**
        rondas_ganadas_humano = 0
        rondas_ganadas_maquina = 0
        turno = mano_actual

        for ronda in range(3):
            print(f"\nRonda {ronda + 1}")
            print(f"Tus cartas restantes: {cartas_humano}")
            print(f"Cartas restantes de la máquina: {cartas_maquina}")

            if turno == "humano":
                carta_humano = jugador_humano(cartas_humano)
                carta_maquina = jugador_aleatorio(cartas_maquina)
                print(f"Tú juegas: {carta_humano} | La máquina responde: {carta_maquina}")
            else:
                carta_maquina = jugador_aleatorio(cartas_maquina)
                print(f"La máquina juega: {carta_maquina}")
                carta_humano = jugador_humano(cartas_humano)
                print(f"Tú respondes: {carta_humano}")
    

                # Comparar fuerza en Truco
                if fuerza_truco(carta_humano) < fuerza_truco(carta_maquina):  # Menor número = más fuerte
                    rondas_ganadas_humano += 1
                    print("Ganas esta ronda.")
                    turno = "humano"
                elif fuerza_truco(carta_humano) > fuerza_truco(carta_maquina):
                    rondas_ganadas_maquina += 1
                    print("La máquina gana esta ronda.")
                    turno = "maquina"
                else:
                    print("Empate en esta ronda.")

        # Determinar ganador del Truco
        ganador = (
            "humano" if rondas_ganadas_humano > rondas_ganadas_maquina else
            "maquina" if rondas_ganadas_maquina > rondas_ganadas_humano else
            None
        )

        if ganador:
            puntos_humano, puntos_maquina = asignar_puntos_truco(
                ganador, truco_cantado, puntos_humano, puntos_maquina
            )
        else:
            print("Empate en las rondas del Truco. No se otorgan puntos.")

        print(f"\nPuntuación tras el Truco: Tú {puntos_humano} | Máquina {puntos_maquina}")

        # Alternar quién es mano en la siguiente mano
        mano_actual = "humano" if mano_actual == "maquina" else "maquina"

    # Resultado final
    print(f"\n¡Fin de la partida! {'Ganaste' if puntos_humano >= puntaje_objetivo else 'La máquina ganó'}")
    return puntos_humano, puntos_maquina