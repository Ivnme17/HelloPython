# Dates

import datetime

def imprimirFecha(fecha):
    print(fecha.hour)
    print(fecha.minute)
    print(fecha.second)
    print(fecha.microsecond)
    print(fecha.date())
    print(fecha.day)
    print(fecha.month)
    print(fecha.year)
    print(fecha.timestamp())


now = datetime.datetime.now()
imprimirFecha(now)

'''Tambien podriamos hacerlo asi si solo queremos importar datetime del modulo datetime
from datetime import datetime

now = datetime.now()
print(now)'''

year_2027 = datetime.datetime(2027, 1, 1)

imprimirFecha(year_2027)

from datetime import time

current_time = time(22, 7, 45)
print(current_time)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
# Podemos darle el valor de la fecha actual
current_date = date.today()
print(current_date)

print(current_date.day)
print(current_date.month)
print(current_date.year)

# O también podemos darle un valor específico
current_date = date(2025, 10, 14)
print(current_date)

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year + 1, current_date.month, current_date.day)
print(current_date.year)

# Diferencia entre fechas
diff = year_2027 - now
print(diff)

# Diferencia entre fechas
diff = year_2027.date() - current_date
print(diff)

# Timedelta - Operaciones con fechas
from datetime import timedelta

time_delta = timedelta()
print(time_delta)

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(200, 100, 300, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)