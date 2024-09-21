import platform
from datetime import datetime

print("Nome maquina:..........", platform.node())
print("Arquitetura:...........", platform.architecture())
print("Sistema Operacional:...", platform.system())
print("Versao do SO:..........", platform.release())
print("Processador:...........", platform.processor())
print("Versao do Python:......", platform.python_version())

print("\nAgora:...", datetime.now())
print("Ano:.....", datetime.now().year)
print("Hora:....", datetime.now().hour)
print("Mes:.....", datetime.now().month)
