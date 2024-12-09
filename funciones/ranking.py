# Función para actualizar el ranking (guardar los puntajes)
def actualizar_ranking(nombre: str, puntos: int, archivo: str = "ranking.txt") -> None:
    """
    Actualiza el ranking con el nombre del jugador y sus puntos.
    Si el archivo no existe, lo crea.
    """
    try:
        with open(archivo, "a", encoding="utf-8") as file:
            file.write(f"{nombre}, {puntos}\n")
    except Exception as e:
        print(f"Error al actualizar el ranking: {e}")

# Función para mostrar el ranking (ordenado por puntos)
def mostrar_ranking(archivo: str = "ranking.txt") -> None:
    """
    Muestra el ranking de jugadores ordenado por puntos.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            ranking = [linea.strip() for linea in file.readlines()]
        
        if not ranking:
            print("Aún no hay jugadores en el ranking.")
            return
        
        # Ordenar el ranking por puntos (de mayor a menor)
        ranking.sort(key=lambda x: int(x.split(",")[1]), reverse=True)

        print("\nRanking de jugadores:")
        for i, entrada in enumerate(ranking, start=1):
            nombre, puntos = entrada.split(", ")
            print(f"{i}. {nombre} - {puntos} puntos")

    except FileNotFoundError:
        print("No se encontró el archivo de ranking.")
    except Exception as e:
        print(f"Error al mostrar el ranking: {e}")