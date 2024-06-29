import json
import datetime


precios_pizzas = {
    "Margarita": {"Pequeña": 5500, "Mediana": 8500, "Familia": 11000},
    "Mexicana": {"Pequeña": 7000, "Mediana": 10000, "Familia": 13000},
    "Barbacoa": {"Pequeña": 6500, "Mediana": 9500, "Familia": 12500},
    "Vegetariana": {"Pequeña": 5000, "Mediana": 8000, "Familia": 10500}
}


descuentos = {
    "Estudiante diurno": 0.15,
    "Estudiante vespertino": 0.18,
    "Administrativo": 0.11
}


ventas = []


def registrar_venta():
    cliente = input("Ingrese el nombre del cliente: ")
    tipo_usuario = input("Ingrese el tipo de usuario (Estudiante diurno, Estudiante vespertino, Administrativo): ")
    while tipo_usuario not in descuentos:
        tipo_usuario = input["Tipo de usuario": tipo_usuario,]

    tipo_pizza = input("Ingrese el tipo de pizza (Margarita, Mexicana, Barbacoa, Vegetariana): ")
    while tipo_pizza not in precios_pizzas:
        tipo_pizza = input["Tipo de pizza": tipo_pizza,]

    tamaño = input("Ingrese el tamaño de la pizza (Pequeña, Mediana, Familia): ")
    while tamaño not in precios_pizzas[tipo_pizza]:
        tamaño = input["Tamaño":tamaño,]

    precio_base = precios_pizzas[tipo_pizza][tamaño]
    precio_final = precio_base * (1 - descuentos[tipo_usuario])

    
    venta = {
        "Cliente": cliente,
        "Tipo de usuario": tipo_usuario,
        "Tipo de pizza": tipo_pizza,
        "Tamaño": tamaño,
        "Precio": precio_final,
        "Fecha y hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ventas.append(venta)
    print("Venta registrada exitosamente.")


def mostrar_ventas():
    for idx, venta in enumerate(ventas, start=1):
        print(f"Venta {idx}: Cliente: {venta['Cliente']}, Tipo de pizza: {venta['Tipo de pizza']}, Tamaño: {venta['Tamaño']}, Precio: ${venta['Precio']}, Fecha y hora: {venta['Fecha y hora']}")


def buscar_por_cliente():
    cliente_buscar = input("Ingrese el nombre del cliente para buscar: ")
    encontradas = [venta for venta in ventas if venta["Cliente"] == cliente_buscar]
    if encontradas:
        for idx, venta in enumerate(encontradas, start=1):
            print(f"Venta {idx}: Tipo de pizza: {venta['Tipo de pizza']}, Tamaño: {venta['Tamaño']}, Precio: ${venta['Precio']}, Fecha y hora: {venta['Fecha y hora']}")
    else:
        print(f"No se encontraron ventas para {cliente_buscar}.")


def guardar_ventas():
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo, indent=4)
    print("Ventas guardadas en el archivo 'ventas.json'.")


def cargar_ventas():
    global ventas
    try:
        with open("ventas.json", "r") as archivo:
            ventas = json.load(archivo)
        print("Ventas cargadas desde el archivo 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'.")


def generar_boleta():
    cliente = input("Ingrese el nombre del cliente para generar la boleta: ")
    encontradas = [venta for venta in ventas if venta["Cliente"] == cliente]
    if encontradas:
        boleta = {
            "Cliente": cliente,
            "Detalles": []
        }
        for venta in encontradas:
            detalle = {
                "Tipo de pizza": venta['Tipo de pizza'],
                "Tamaño": venta['Tamaño'],
                "Precio": venta['Precio'],
                "Fecha y hora": venta['Fecha y hora']
            }
            boleta["Detalles"].append(detalle)

        nombre_archivo = f"boleta_{cliente}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(nombre_archivo, "w") as archivo_boleta:
            json.dump(boleta, archivo_boleta, indent=4)
        print(f"Boleta generada exitosamente como '{nombre_archivo}'.")
    else:
        print(f" ventas para {cliente}.")


def anular_venta():
    cliente = input("Ingrese el nombre del cliente para anular la venta: ")
    encontradas = [venta for venta in ventas if venta["Cliente"] == cliente]
    if encontradas:
        ventas.remove(encontradas[0])
        print(f"Venta de {cliente} anulada exitosamente.")
    else:
        print(f"Venta anulada con exito como'{cliente}.")


def menu():
    while True:
        print("\n----- Sistema de ventas de pizzas DUOC UC -----")
        print("1. Registrar una venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar ventas por cliente")
        print("4. Guardar las ventas en un archivo")
        print("5. Cargar las ventas desde un archivo")
        print("6. Generar Boleta")
        print("7. Anular venta")
        print("8. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            buscar_por_cliente()
        elif opcion == "4":
            guardar_ventas()
        elif opcion == "5":
            cargar_ventas()
        elif opcion == "6":
            generar_boleta()
        elif opcion == "7":
            anular_venta()
        elif opcion == "8":
            print("Gracias por utilizar el sistema de ventas de pizzas DUOC UC.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
