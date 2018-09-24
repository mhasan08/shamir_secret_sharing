import random


# referred from wiki
def _extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y


def mod_div(num, den, p):
    inv, de = _extended_gcd(den, p)
    return num * inv


# referred from wiki
def lagrange(x, xlist, ylist, p):

    def PI(vals):
        accum = 1
        for v in vals:
            accum *= v
        return accum

    nums = []
    dens = []
    for i in range(0, len(xlist)):
        others = list(xlist)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)

    num = 0
    for j in range(0, len(xlist)):
        num = num + mod_div(nums[j] * den * ylist[j] % p, dens[j], p)

    return (mod_div(num, den, p) + p) % p


def evaluate_modulus_poly(_secret, list_of_num, x_val, prime):
    poly_sum = 0
    for i in range(0, len(list_of_num)):
        poly_sum = poly_sum + list_of_num[i] * (x_val ** (i + 1))
    return (poly_sum + _secret) % prime


def create_random_coefficients(minimum, prime):
    list_of_random_int = []
    for i in range(0, minimum - 1):
        list_of_random_int.append(random.randint(10, prime - 1))
    return list_of_random_int
