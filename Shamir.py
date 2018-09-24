'''
Author: Munawar Hasan

'''

import random
from utils import Helper
from utils import SecretShare

_PRIME = 2**521 - 1
_BYTES = 65
_MINIMUM = 3
_SHARES = 10

f = open("data/flower.jpg", "rb")
image_bytes = f.read()
f.close()

image_byte_array = bytearray(image_bytes)

length = len(image_byte_array)
#print(len(image_byte_array))

stubs = int(length / _BYTES) + 1
#print(stubs)

stubs_int_list = []

counter = 0
for i in range(0, int(length / _BYTES)):
    _bytes = image_byte_array[counter: counter + _BYTES]
    stubs_int_list.append(int.from_bytes(_bytes, byteorder='little'))
    counter = counter + _BYTES

stubs_int_list.append(int.from_bytes(image_byte_array[counter: length], byteorder='little'))

#print(stubs_int_list)

# generate shares

w = _SHARES + 1
h = len(stubs_int_list)

Matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(0, len(stubs_int_list)):
    list_of_coefficients = SecretShare.create_random_coefficients(_MINIMUM, _PRIME)

    # evaluate all the shares wrt this int
    for j in range(0, _SHARES + 1):
        Matrix[i][j] = SecretShare.evaluate_modulus_poly(stubs_int_list[i], list_of_coefficients, j, _PRIME)

# Matrix is the secret; any _MINIMUM value pairs can be distributed

# recover the values

shared_poly_index = []
for i in range(0, _MINIMUM):
    index = random.randint(1, _SHARES)
    while index in shared_poly_index:
        index = random.randint(1, _SHARES)
    shared_poly_index.append(index)
shared_poly_index.sort()


recovered_stubs_int_list = []

for i in range(0, h):
    p_list = []
    for j in range(0, len(shared_poly_index)):
        p_list.append(Matrix[i][shared_poly_index[j]])
    value = SecretShare.lagrange(0, shared_poly_index, p_list, _PRIME)

    recovered_stubs_int_list.append(value)

#print(len(recovered_stubs_int_list))

Helper.check_recovered_values(stubs_int_list, recovered_stubs_int_list)

Helper.create_image_from_int_list(recovered_stubs_int_list, _BYTES)



