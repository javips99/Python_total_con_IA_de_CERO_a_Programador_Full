
### Paquete de ejemplo
# Usamos el comando pip install colorama 

# Para usar colorama:
# 1. Instalar: pip install colorama
# 2. Importar: from colorama import Fore, Style, init
# 3. Activar: init(autoreset=True)
# 4. Usar colores en consola, por ejemplo:
#    print(Fore.GREEN + "Mensaje en verde" + Style.RESET_ALL)
#    print(Style.BRIGHT + Fore.BLUE + "Mensaje resaltado" + Style.RESET_ALL)

from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.RED + "Error")
print(Fore.GREEN + "Correcto")
print(Fore.YELLOW + "Aviso")
print(Style.BRIGHT + Fore.BLUE + "Importante")