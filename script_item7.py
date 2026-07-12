from netmiko import ConnectHandler

# Definición del dispositivo (usando tus credenciales)
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',
    'username': 'cisco',
    'password': 'cisco123!',
}

# Conectar al router
connection = ConnectHandler(**router)

# 1. Configurar EIGRP Nombrado (IPv4/IPv6)
print("--- Configurando EIGRP Nombrado ---")
commands = [
    'router eigrp MODO_LAB',
    'address-family ipv4 unicast autonomous-system 100',
    'af-interface Loopback33',
    'passive-interface',
    'exit-af-interface',
    'exit-address-family',
    'address-family ipv6 unicast autonomous-system 100',
    'af-interface Loopback33',
    'passive-interface',
    'exit-af-interface',
    'exit-address-family'
]
connection.send_config_set(commands)

# 2. Mostrar resultado EIGRP
print("\n--- Show Running-config EIGRP ---")
print(connection.send_command("show running-config | section eigrp"))

# 3. Obtener IP y estado de interfaces
print("\n--- Estado de Interfaces ---")
print(connection.send_command("show ip interface brief"))

# 4. Obtener running-config
print("\n--- Running-config completo ---")
print(connection.send_command("show running-config"))

# 5. Obtener show version
print("\n--- Show Version ---")
print(connection.send_command("show version"))

connection.disconnect()