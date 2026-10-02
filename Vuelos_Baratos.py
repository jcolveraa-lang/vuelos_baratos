import heapq


class SistemaVuelos:
    def __init__(self):
        # Base de datos ficticia de vuelos usando Lista de Adyacencia
        self.grafo = {
            "Quito": [("Guayaquil", 60), ("Cuenca", 50), ("Coca", 40)],
            "Guayaquil": [("Quito", 60), ("Cuenca", 30), ("Baltra", 120), ("Manta", 45)],
            "Cuenca": [("Quito", 50), ("Guayaquil", 30), ("Baltra", 150)],
            "Coca": [("Quito", 40)],
            "Baltra": [("Guayaquil", 120), ("Cuenca", 150)],
            "Manta": [("Guayaquil", 45)]
        }

    def reporteria(self):
        """Visualizar y consultar la estructura de datos."""
        print("\n--- REPORTERÍA DE RED DE VUELOS DISPONIBLES ---")
        for origen, destinos in self.grafo.items():
            print(f"Desde {origen}:")
            for destino, costo in destinos:
                print(f"  --> Hacia {destino} | Costo: ${costo}")
        print("--------------------------------------------------")

    def buscar_vuelo_barato(self, origen, destino):
        """Encuentra la ruta de menor costo usando el Algoritmo de Dijkstra."""
        if origen not in self.grafo or destino not in self.grafo:
            return None, float('inf')

        # Cola de prioridad: (costo_acumulado, ciudad_actual, camino)
        pq = [(0, origen, [origen])]
        visitados = set()

        while pq:
            costo_actual, ciudad_actual, camino = heapq.heappop(pq)

            if ciudad_actual == destino:
                return camino, costo_actual

            if ciudad_actual in visitados:
                continue

            visitados.add(ciudad_actual)

            for vecino, costo in self.grafo.get(ciudad_actual, []):
                if vecino not in visitados:
                    heapq.heappush(pq, (costo_actual + costo, vecino, camino + [vecino]))

        return None, float('inf')


def menu():
    sistema = SistemaVuelos()
    while True:
        print("\n=== SISTEMA DE BÚSQUEDA DE VUELOS BARATOS (UEA) ===")
        print("1. Mostrar todos los vuelos disponibles (Reportería)")
        print("2. Buscar la ruta de vuelo más barata")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            sistema.reporteria()
        elif opcion == "2":
            origen = input("Ingrese ciudad de origen (ej. Coca): ").strip().capitalize()
            destino = input("Ingrese ciudad de destino (ej. Baltra): ").strip().capitalize()

            camino, costo = sistema.buscar_vuelo_barato(origen, destino)

            if camino:
                print(f"\n¡RUTA MÁS BARATA ENCONTRADA!")
                print(f"Ruta: {' -> '.join(camino)}")
                print(f"Costo Total: ${costo}")
            else:
                print(f"\nNo existe una ruta disponible entre {origen} y {destino}.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()1