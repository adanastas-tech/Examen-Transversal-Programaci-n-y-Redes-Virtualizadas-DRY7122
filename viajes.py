import requests

# ===========================================
# CONFIGURACIÓN
# ===========================================

API_KEY = "f52f36aa-6d13-4a8f-9a2f-a2702ec6a606"

URL_GEOCODE = "https://graphhopper.com/api/1/geocode"
URL_ROUTE = "https://graphhopper.com/api/1/route"


# ===========================================
# OBTENER COORDENADAS
# ===========================================

def obtener_coordenadas(ciudad, pais):

    parametros = {
        "q": f"{ciudad}, {pais}",
        "limit": 1,
        "key": API_KEY
    }

    respuesta = requests.get(URL_GEOCODE, params=parametros)

    if respuesta.status_code != 200:
        return None

    datos = respuesta.json()

    if not datos["hits"]:
        return None

    lat = datos["hits"][0]["point"]["lat"]
    lng = datos["hits"][0]["point"]["lng"]

    return lat, lng


# ===========================================
# CALCULAR RUTA
# ===========================================

def calcular_ruta(origen, destino, perfil):

    parametros = [
        ("point", f"{origen[0]},{origen[1]}"),
        ("point", f"{destino[0]},{destino[1]}"),
        ("profile", perfil),
        ("locale", "es"),
        ("instructions", "true"),
        ("calc_points", "false"),
        ("key", API_KEY)
    ]

    respuesta = requests.get(URL_ROUTE, params=parametros)

    if respuesta.status_code != 200:
        print("Error HTTP:", respuesta.status_code)
        return None

    datos = respuesta.json()

    if "paths" not in datos:
        print(datos)
        return None

    return datos


# ===========================================
# MOSTRAR RESULTADOS
# ===========================================

def mostrar_resultados(datos):

    ruta = datos["paths"][0]

    # Distancia
    distancia_km = ruta["distance"] / 1000
    distancia_millas = distancia_km * 0.621371

    # Tiempo
    tiempo_segundos = ruta["time"] / 1000
    horas = int(tiempo_segundos // 3600)
    minutos = int((tiempo_segundos % 3600) // 60)

    print("\n==============================")
    print("RESULTADO DEL VIAJE")
    print("==============================")

    print(f"\nDistancia en kilómetros : {distancia_km:.2f} km")
    print(f"Distancia en millas     : {distancia_millas:.2f} mi")
    print(f"Duración del viaje      : {horas} horas {minutos} minutos")

    print("\nConsulta realizada correctamente.")
   

# ==========================================
# MENÚ PRINCIPAL
# ===========================================

while True:

    print("\n====================================")
    print("CALCULADORA DE RUTAS")
    print("====================================")

    print("Escriba uno de los siguientes medios:")

    print("Auto")

    print("Bicicleta")

    print("Caminando")

    print("S = Salir")

    transporte = input("\nSeleccione: ").strip().lower()

    if transporte == "s":
        print("\nPrograma finalizado.")
        break

    if transporte in ["auto", "car", "vehiculo", "vehículo"]:

        perfil = "car"

    elif transporte in ["bicicleta", "bike"]:

        perfil = "bike"

    elif transporte in ["caminando", "caminar", "foot"]:

        perfil = "foot"

    else:

        print("\nMedio de transporte no válido.")

        continue

    ciudad_origen = input("\nCiudad de Chile: ").strip()

    ciudad_destino = input("Ciudad de Argentina: ").strip()

    origen = obtener_coordenadas(ciudad_origen, "Chile")

    if origen is None:

        print("\nNo se encontró la ciudad chilena.")

        continue

    destino = obtener_coordenadas(ciudad_destino, "Argentina")

    if destino is None:

        print("\nNo se encontró la ciudad argentina.")

        continue

    datos = calcular_ruta(origen, destino, perfil)

    if datos is None:

        print("\nNo fue posible calcular la ruta.")

        continue

    mostrar_resultados(datos)

    break
    