from colorama.ansi import Fore
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
import time
from colorama import Fore
{Fore.RED}
print('\033[36m'"""
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                            
===================By Qu3ti==========================
""")
{Fore.RESET}

data=input('Ingresa el numero: ')

numdata = phonenumbers.parse(data)
zone = timezone.time_zones_for_number(numdata)

geo = geocoder.description_for_number(numdata, 'es')

carr = ("Carrier: "+carrier.name_for_number (numdata, 'es'))

print("Espera...")
time.sleep(0.4)
print('\033[32m'"Listo! ")
time.sleep(0.2)

print(numdata)
print(zone)
print(geo)
print(carr)
time.sleep(15)
