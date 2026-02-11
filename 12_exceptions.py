# Excepciones

numberOne = 5 
numberTwo = 1
numberTwo = "1"


# Try except
try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except:
    # Se ejecuta si se da una excepcion
    print("No se puede realizar la operación")


# Try except else

try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except:
    print("No se puede realizar la operación")
else:
    # Se ejecuta si no se da una excepcion
    print("La operación continua correctamente")


# Try except else finally

try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except:
    print("No se puede realizar la operación")
else:
    # Se ejecuta si no se da una excepcion
    print("La operación continua correctamente")
finally:
    # Se ejecuta si o si
    print("La operación continua")


# Try except else finally

try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except: # OBLIGATORIO
    print("No se puede realizar la operación")
else: # OPCIONAL
    print("La operación continua correctamente")
finally: # OPCIONAL
    print("La operación continua")

# Try except con tipo de excepcion
try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except TypeError:
    # Se ejecuta si se da una excepcion
    print("No se puede realizar la operación")

'''try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except ValueError:
    # Se ejecuta si se da una excepcion
    print("No se puede realizar la operación")'''


try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except (TypeError, ValueError):
    # Se ejecuta si se da una excepcion
    print("No se puede realizar la operación")


try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except ValueError:
    # Se ejecuta si se da una excepcion
    print("No se puede realizar la operación")
except TypeError:
    # Se ejecuta si se da una excepcion
    print("No se puede realizar la operación")

# Captura de la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print("Se puede realizar la operación")
except ValueError as error:
    # Se ejecuta si se da una excepcion
    print(error)
except Exception as excepcion:
    # Controla cualquier tipo de error
    print(excepcion)
