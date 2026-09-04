#Registrar las edades de n cantidad de personas y mostrar la edad mas alta y mas baja y la cantidad de personas registradas.
ages = []

def addAge(age):
    ages.append(age)

def getMaxAge():
    maxAge = ages[0]
    for age in ages:
        if age > maxAge:
            maxAge = age
    return maxAge

def getMinAge():
    minAge = ages[0]
    for age in ages:
        if age < minAge:
            minAge = age
    return minAge

def showSize():
    return len(ages)

def showAges():
    return ages

while True:
    try:
        age = int(input("Dime tu edad: "))
        if(age > 3):
            addAge(age)
        else:
            print("Debe ser un número mayor a 3")

        answer = input("Ingresa otro [S - N]: ")
        if answer.upper() != "S":
            break

    except ValueError:
        print("Debe ingresar un entero. ")


print("Mostrar edades")
print(f"Cantidad de edades registradas: {showSize()}")
print(showAges())
print(f"Edad mas vieja: {getMaxAge()}")
print(f"Edad mas joven: {getMinAge()}")




