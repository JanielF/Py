### Exceptions #Handling##

numberOne = 5
numberTwo = 1
numberTwo = "1"

#try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #se ejecuta si hay una exceptio (error) en el codigo
    print("Se ha producido un error")

#try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #Opcional
    #Esto se ejecutara si no hay ninguna exception.
    print("La ejecucion continua correctamente")
finally: #Opcional
    #Se ejecuta siempre este o no este mal el codigo.
    print("La ejecucion continua")

# Exceptions por tipo (Para capturar errores muy concretos).

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    #se ejecuta si hay una exceptio (error) en el codigo
    print("Se ha producido un ValueError")
except TypeError:
    #se ejecuta si hay una exceptio (error) en el codigo
    print("Se ha producido un TypeError")

# Captura de la informacion de la exception.

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    #se ejecuta si hay una exceptio (error) en el codigo
    print(error)
except Exception as exception:
    print(exception)