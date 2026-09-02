#sumar dos numeros y mostrar el resultado
#Parametro es la variable que se define cuando se crea la función
def getSum(number1, number2):
    return number1 + number2

def showResult(message, result):
    return f"{message} {result}"

print("Dime un numero: ")
num1 = float(input())
print("Dime otro numero: ")
num2 = float(input())
#Argumento  es el valor que se envía a la función cuando se llama.
sum = getSum(num1, num2)
print(showResult("La suma es:", sum))

