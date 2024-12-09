import random
TRUCO_PUNTOS = {
    "truco": 2,
    "retruco": 3,
    "vale_cuatro": 4
}

SIGUIENTE_CANTO = {
    None: "truco",
    "truco": "retruco",
    "retruco": "vale_cuatro"
}
def gestionar_truco(turno: str, truco_cantado: str, puntos_humano: int, puntos_maquina: int ) -> tuple[str, int, int, bool]:
    """
    Gestiona el canto del Truco, Re-Truco y Vale Cuatro.
    Argumentos:
        turno (str): 'humano' o 'maquina', indicando quién inicia el turno.
        truco_cantado (str): Estado actual del truco ('truco', 'retruco', 'vale_cuatro').
        puntos_humano (int): Puntos actuales del jugador humano.
        puntos_maquina (int): Puntos actuales de la máquina.
    Returns:
        Tuple[str, int, int, bool]: Nuevo estado del truco, puntos adicionales para humano y máquina, rechazo (True/False).
    """
    siguiente_canto = SIGUIENTE_CANTO.get(truco_cantado)
    rechazo = False

    if turno == "humano":
        # Mostrar opciones al jugador
        print(f"\nOpciones disponibles:")
        print(f"[1] Cantar {siguiente_canto.capitalize()} | [2] Aceptar el canto | [3] Rechazar")
        decision = int(input("Elige una opción: "))

        if decision == 1:
            print(f"Has cantado {siguiente_canto.capitalize()}.")
            truco_cantado = siguiente_canto
            turno = "maquina"  # Cambiar turno
        elif decision == 2:
            print("Has aceptado el canto.")
        elif decision == 3:
            print(f"Rechazaste el canto. La máquina gana {TRUCO_PUNTOS.get(truco_cantado, 1)} puntos.")
            puntos_maquina += TRUCO_PUNTOS.get(truco_cantado, 1)
            rechazo = True

    else:  # Turno de la máquina
        decision_maquina = decidir_maquina(truco_cantado)

        if decision_maquina == "cantar":
            print(f"La máquina canta {siguiente_canto.capitalize()}.")
            truco_cantado = siguiente_canto
            turno = "humano"  # Cambiar turno
        elif decision_maquina == "aceptar":
            print("La máquina acepta el canto.")
        elif decision_maquina == "rechazar":
            print(f"La máquina rechaza el canto. Tú ganas {TRUCO_PUNTOS.get(truco_cantado, 1)} puntos.")
            puntos_humano += TRUCO_PUNTOS.get(truco_cantado, 1)
            rechazo = True

    return truco_cantado, puntos_humano, puntos_maquina, rechazo

def decidir_maquina(truco_cantado: str) -> str:
    """
    Decide la acción de la máquina ante un canto del Truco.
    Argumentos:
        truco_cantado (str): Estado actual del truco ('truco', 'retruco', 'vale_cuatro').
    Returns:
        str: Acción tomada por la máquina ('cantar', 'aceptar', 'rechazar').
    """
    # Lógica básica de decisión de la máquina
    if truco_cantado is None:
        return random.choice(["cantar", "aceptar"])
    elif truco_cantado == "truco":
        return random.choice(["cantar", "aceptar", "rechazar"])
    elif truco_cantado == "retruco":
        return random.choice(["aceptar", "rechazar"])
    else:  # Vale Cuatro
        return "rechazar"  # Supongamos que no arriesga siempre.

def asignar_puntos_truco(ganador: str, truco_cantado: str, puntos_humano: int, puntos_maquina: int) -> tuple[int, int]:
    """
    Asigna puntos al ganador del truco.
    Argumentos:
        ganador (str): 'humano' o 'maquina'.
        truco_cantado (str): Último canto aceptado ('truco', 'retruco', 'vale_cuatro').
        puntos_humano (int): Puntos actuales del humano.
        puntos_maquina (int): Puntos actuales de la máquina.
    Returns:
        Tuple[int, int]: Puntos actualizados del humano y la máquina.
    """
    puntos_ganados = TRUCO_PUNTOS.get(truco_cantado, 1)

    if ganador == "humano":
        puntos_humano += puntos_ganados
        print(f"Tú ganas el Truco y obtienes {puntos_ganados} puntos.")
    elif ganador == "maquina":
        puntos_maquina += puntos_ganados
        print(f"La máquina gana el Truco y obtiene {puntos_ganados} puntos.")

    return puntos_humano, puntos_maquina
