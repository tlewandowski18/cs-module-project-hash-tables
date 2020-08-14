# Your code here
import math

powers_index = {}
for i in range(2, 14):
    powers_index[i] = [i**3, i**4, i**5]


factorial_index = {}
for key, value in powers_index.items():
    new_list = []
    for num in value:
        new_list.append(math.factorial(num))
    factorial_index[key] = new_list


floor_division_index = {}

for key, value in factorial_index.items():
    new_list = [value[0] // (key + 3), value[1] // (key + 4), value[2] // (key + 5)]
    floor_division_index[key] = new_list

modulo_index = {}
for key, value in floor_division_index.items():
    new_list = []
    for num in value:
        new_list.append(num % 982451653)
    modulo_index[key] = new_list

# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v

def slowfun(x, y):
#     """
#     Rewrite slowfun_too_slow() in here so that the program produces the same
#     output, but completes quickly instead of taking ages to run.
#     """
#     # Your code here
    if y == 3:
        return modulo_index[x][0]
    elif y == 4:
        return modulo_index[x][1]
    else:
        return modulo_index[x][2]



# Do not modify below this line!
import random

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
