# Lambda
# Son funciones anonimas que se pueden usar para crear funciones simples
sum_two_values = lambda a, b: a + b
print(sum_two_values(2, 4))

multiply_values = lambda a, b: a * b
print(multiply_values(2, 4))

def sum_three_values(a):
    return lambda b, c: a + b + c

# my_sum = sum_three_values(a)(b, c)
my_sum = sum_three_values(1)(2, 3)
print(my_sum)
# o tambien se puede hacer directamente
print(sum_three_values(1)(2, 3))

# sum_value_and_lambda (value, funcion lambda definida anteriormente) y retorna -> lambda a, b: value + sum_two_values(a, b)
def sum_value_and_lambda(value, sum_two_values):
    return lambda a, b: value + sum_two_values(a, b)

my_sum_lambda = sum_value_and_lambda(1, sum_two_values)
print(my_sum_lambda(2, 3))