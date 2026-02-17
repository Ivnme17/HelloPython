# Funciones de orden superior

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

# Las funciones de orden superior son funciones que pueden usar otras funciones dentro de ellas
def sum_two_values_and_add_one(a, b):
    return sum_one(a + b)

print(sum_two_values_and_add_one(1, 2)) 

# Funcion que recibe otra funcion como parametro
def sum_two_values_and_add_one(a, b, f_sum):
    return f_sum(a + b)


print(sum_two_values_and_add_one(1, 2, sum_one)) 
print(sum_two_values_and_add_one(1, 2, sum_five)) 

# Closures o clausuras

def sum_ten():
    def add(value):
        return value + 10
    return add


add_closure = sum_ten()
print(add_closure(5))

# Built-in higher order functions

numbers=[2, 5, 10, 22]

# Map
# Con funcion lambda
print(list(map(lambda x: x * 2, numbers)))

# Con funcion definida
def multiply_two(x):
    return x * 2

print(list(map(multiply_two, numbers)))


# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))


# Reduce

def sum_two_values( a, b):
    print(a, "+", b)
    return a + b

print(reduce(sum_two_values, numbers))