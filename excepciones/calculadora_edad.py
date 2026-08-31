import subprocess
while True:
    try:
        subprocess.run("cls", shell=True)
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Ingresa un valor numérico.")
        input("Presione enter para continuar...")

print("Edad registrada:", edad)