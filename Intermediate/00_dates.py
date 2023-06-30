### Dates ###

from datetime import datetime #de esta forma no se tiene que redundar sobre el mismo modulo(import).

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2024 = datetime(2024,1,1) #Lo minimo que se necesita para definir un año.

print_date(year_2024)

from datetime import time #objeto que sirve para capturar tiempo (se tiene que rellenar manual).

current_time = time(10,20,10)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date #solo captura el año, mes y dia.

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023,6,8)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,current_date.month + 1,current_date.day)

print(current_date.month)

diff = year_2024- now
print(diff)

diff = year_2024.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200,100,100,weeks=10)
end_timedelta = timedelta(300,100,100,weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)