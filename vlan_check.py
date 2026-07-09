# Script para determinar el rango de una VLAN

try:
    vlan = int(input("Ingrese el número de VLAN a verificar: "))

    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} corresponde al rango NORMAL.")
    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} corresponde al rango EXTENDIDO.")
    else:
        print(f"El número {vlan} no es un número de VLAN válido (debe ser entre 1 y 4094).")
        
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
