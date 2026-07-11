from ncclient import manager
from ncclient.xml_ import to_ele

host = '192.168.56.102'
user = 'cisco'
password = 'cisco123!'

config_xml = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Anastas-Escobar</hostname>
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

try:
    with manager.connect(host=host, port=830, username=user, password=password, 
                         hostkey_verify=False, device_params={'name': 'csr'}) as m:
        
        print("Enviando configuración vía NETCONF...")
        # edit_config aplica los cambios
        m.edit_config(target='running', config=config_xml)
        print("¡Configuración aplicada con éxito!")
        
except Exception as e:
    print(f"Error en NETCONF: {e}")